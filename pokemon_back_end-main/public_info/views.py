from django.shortcuts import render

# Create your views here.
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from .models import  Publicinfo
# from .serializers import PokemonSerializer, TypeSerializer, PublicinfoSerializer
from .serializers import  PublicinfoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

# Create your views here.
@require_GET
def get_Publicinfo(request):
    # get 5 info
    raw_query = '''
        SELECT * FROM Pokemon.public_info LIMIT 10
    '''
    data = executeSQL(raw_query)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_POST
def search_public_by_id(request):
    """
    Get 5 info with id >= given data
    """
    data = json.loads(request.body)
    info = Publicinfo.objects.filter(user_id__gte=data['user_id'])[:10]
    results = PublicinfoSerializer(info, many=True).data
    return JsonResponse(results, safe=False)


@require_GET
def get_Public_statistics(request):
    """
    Advanced Query function
    """
    return JsonResponse(executeSQL(
        '''
            SELECT pokemon_ID, count(*) AS training_count
            FROM
            (SELECT hp, hp_T, training.pokemon_ID
            FROM pokemon JOIN training ON pokemon.pokemon_ID = training.pokemon_ID
            WHERE hp > hp_T
            ) AS temp
            GROUP BY pokemon_ID
            ORDER BY training_count DESC
            LIMIT 30;
        '''
    ), safe=False)


@csrf_exempt
@require_POST
def create_public(request):
    """
    Create a info with given data
    """
    data = json.loads(request.body)
    info = Publicinfo(

        user_id = random.randint(100600, 101000),
        training_id = random.randint(1, 1000),
        share_info = 0,

    )
    info.save()

    return JsonResponse({'message': 'success'})


@csrf_exempt
@require_POST
def update_public(request):
    try:
        data = json.loads(request.body)
         
        if not data["share_info"]:
            sql = f' update public_info set share_info = {False} where user_id="{data["user_id"]}" and training_id={data["training_id"]};'
        else:
            sql = f' update public_info set share_info = {True} where user_id="{data["user_id"]}" and training_id={data["training_id"]};'

        print(sql)
            
        with connection.cursor() as cursor:
            cursor.execute(sql)

    except Publicinfo.DoesNotExist:
        return JsonResponse({'message': 'Public Info does not exist'}, status=404)

    return JsonResponse({'message': 'success'})


@csrf_exempt
@require_POST
def delete_public(request):
    data = json.loads(request.body)
    raw_query = '''
        DELETE FROM Pokemon.public_info 
        WHERE user_id="{data['user_id']}"
        AND training_id={data['training_id']}
    '''
    try:
        executeSQLWrite(raw_query)
    except Exception:
        return JsonResponse(status=500)

    return JsonResponse({'message': 'success'})