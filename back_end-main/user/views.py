from django.shortcuts import render

# Create your views here.
import json
import random
import string

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from user.models import User
from user.serializers import UserSerializer
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
def get_user(request):
    # get 10 user
    user = User.objects.all()[:10]
    data = UserSerializer(user, many=True).data
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_POST
def search_user_by_id(request):
    """
    Get user by id 
    """
    data = json.loads(request.body)
    user = User.objects.get(user_id=data['user_id'])
    results = UserSerializer(user, many=False).data
    results = [results]
    return JsonResponse(results, safe=False)

@csrf_exempt
@require_POST
def user_exists(request):
    """
    Get user by id 
    """
    data = json.loads(request.body)
    user_exists = User.objects.filter(userEmail=data['email']).count();
    return JsonResponse({ 'exists': not user_exists == 0 }, safe=False)

@require_GET
def advance(request):
    """
    Advanced Query function
    """
    return JsonResponse(executeSQL(
        '''
            (SELECT training_ID, hp_T,  attack_T, specialAttack_T, defense_T, specialDefense_T,speed,legendary
            FROM Pokemon.pokemon join Pokemon.training
            on Pokemon.pokemon.pokemon_ID = Pokemon.training.pokemon_ID
            Where legendary = 1 and specialAttack_T > attack_T and specialDefense_T > defense and hp_T > 100)

                union

            (SELECT training_ID, hp_T,  attack_T, specialAttack_T, defense_T, specialDefense_T,speed,legendary
            FROM Pokemon.pokemon join (
            SELECT pokemon_ID, training_ID, hp_T,  attack_T, specialAttack_T, defense_T, specialDefense_T 
            FROM Pokemon.training  
            WHERE (specialAttack_T > 150 or specialDefense_T > 150) and hp_T > 100
            ) as temp on Pokemon.pokemon.pokemon_ID = temp.pokemon_ID
            Where legendary = 0)
        '''
    ), safe=False)


@csrf_exempt
@require_POST
def create_user(request):
    """
    Create a user with given data
    """
    data = json.loads(request.body)
    user = User(
        user_id=random.randint(101001, 200000),
        userName = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5,7))),
        userPassword = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5,7))),
        userEmail = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(5,7))) + "@gmail.com",
        privacy = random.randint(0,1),
    )
    user.save()

    return JsonResponse({'message': 'success'})



@csrf_exempt
@require_POST
def register(request):
    """
    Create a user with given data
    """
    data = json.loads(request.body)
    user = User(
        user_id='{}'.format(random.randint(101001, 200000)),
        userName = data['email'].split('@')[0],
        userPassword = data['password'],
        userEmail = data['email'],
        privacy = random.randint(0,1),
    )
    user.save()

    results = UserSerializer(user, many=False).data
    print(results)
    return JsonResponse({
        'message': 'register success',
        'user': results
    }, safe=False)


@csrf_exempt
@require_POST
def login(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(userEmail=data["email"])

    except User.DoesNotExist:
        return JsonResponse({'message': 'user does not exist'}, status=404)
    
    if user.userPassword != data['password']:
        return JsonResponse({'message': 'Credential not match'}, status=401)

    results = UserSerializer(user, many=False).data
    return JsonResponse({
        'message': 'login success',
        'user': results
    }, safe=False)


@csrf_exempt
@require_POST
def update_user(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(user_id=data["user_id"])
        user.userName = data["userName"]
        user.userPassword = data["userPassword"]
        user.userEmail= data["userEmail"]
        user.privacy = data["privacy"]
        user.save()

    except User.DoesNotExist:
        return JsonResponse({'message': 'user does not exist'}, status=404)

    return JsonResponse({'message': 'success'})


@csrf_exempt
@require_POST
def delete_user(request):
    try:
        data = json.loads(request.body)
        user = User.objects.get(user_id=data["user_id"])
        user.delete()

    except User.DoesNotExist:
        return JsonResponse({'message': 'user does not exist'}, status=404)

    return JsonResponse({'message': 'success'})





