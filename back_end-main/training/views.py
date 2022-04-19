import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from training.models import Training
from .serializers import TrainingSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from public_info.models import Publicinfo
from public_info.views import delete_public


def executeSQL(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def executeSQLWrite(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)


# Create your views here.
@require_GET
def get_trainings(request, userId):
    # get 5 pokemon
    raw_query = '''
        SELECT * FROM Pokemon.training
        NATURAL JOIN Pokemon.public_info 
        WHERE user_id = {}'''.format(userId)
    trainings = executeSQL(raw_query)

    return JsonResponse(trainings, safe=False)


@require_GET
def all_trainings(request):
    raw_query = '''
        SELECT * FROM Pokemon.training NATURAL JOIN Pokemon.public_info
        WHERE share_info = 1
    '''
    trainings = executeSQL(raw_query)

    return JsonResponse(trainings, safe=False)


@csrf_exempt
@require_POST
def adopt_pokemon(request):
    data = json.loads(request.body)
    training_id = random.randint(120000, 200000)
    training = Training(
        pokemon_id = data['pokemon_id'],
        training_id=training_id,
        hp_T=data['hp'],
        attack_T=data['attack'],
        defense_T=data['defense'],
        specialAttack_T=data['specialAttack'],
        specialDefense_T=data['specialDefense'],
        speed_T=data['speed'],
        height_T=data['height'],
        weight_T=data['weight'],
    )
    training.save()

    raw_query = "INSERT INTO training_has_types VALUES "
    for t in data['types']:
        raw_query += '(%s, "%s"),' % (training_id, t)
    raw_query = raw_query[:-1]
    raw_query += ';'

    executeSQLWrite(raw_query)

    print(data)
    info = Publicinfo(
        user_id = data['userId'],
        training_id = training_id,
        share_info = 0,
    )
    info.save()

    return JsonResponse({
        'message': 'success',
        'training_id': training_id,
    })


@csrf_exempt
@require_POST
def search_training_by_id(request):
    """
    Get 5 training with id >= given data
    """
    data = json.loads(request.body)
    raw_query = '''
        SELECT * FROM Pokemon.training NATURAL JOIN Pokemon.public_info
        WHERE share_info = 1 AND training_id >= {}
        LIMIT 10
    '''.format(data['training_id'])
    trainings = executeSQL(raw_query)

    return JsonResponse(trainings, safe=False)


@require_GET
def advanced_query(request):
    """
    Advanced Query function
    """
    return JsonResponse(executeSQL(
        '''
        select training_ID, hp_T, attack_T, specialAttack_T, attack, specialAttack, defense_T, specialDefense_T, defense, specialDefense
        from Pokemon.training join Pokemon.pokemon on Pokemon.training.pokemon_ID = Pokemon.pokemon.pokemon_ID
        where attack_T > 120 and specialAttack_T > 120 and attack < 120 and specialAttack < 120

        UNION

        select training_ID, hp_T, attack_T, specialAttack_T, attack, specialAttack, defense_T, specialDefense_T, defense, specialDefense
        from Pokemon.training join Pokemon.pokemon on Pokemon.training.pokemon_ID = Pokemon.pokemon.pokemon_ID
        where defense_T > 170 and specialDefense_T > 170 and defense < 170 and specialDefense < 170

        order by hp_T
        limit 15
        '''
    ), safe=False)


@csrf_exempt
@require_POST
def create_training(request):
    """
    Create a training with given data
    """
    data = json.loads(request.body)
    training = Training(
        pokemon_id = data['pokemon_id'],
        training_id=random.randint(120000, 200000),
        hp_T=data['hp_T'],
        attack_T=data['attack_T'],
        defense_T=data['defense_T'],
        specialAttack_T=data['specialAttack_T'],
        specialDefense_T=data['specialDefense_T'],
        speed_T=data['speed_T'],
        height_T=data['height_T'],
        weight_T=data['weight_T']
    )
    training.save()

    return JsonResponse({
        'message': 'success',
        'training_id': training.training_id,
    })


@csrf_exempt
@require_POST
def update_training(request):
    data = json.loads(request.body)
    try:
        training = Training.objects.get(training_id=data["training_id"])

        training.pokemon_id = data['pokemon_id']
        training.hp_T = data["hp_T"]
        training.attack_T = data["attack_T"]
        training.defense_T = data["defense_T"]
        training.specialAttack_T = data["specialAttack_T"]
        training.specialDefense_T = data["specialDefense_T"]
        training.speed_T = data["speed_T"]
        training.height_T = data["height_T"]
        training.weight_T = data["weight_T"]

        training.save()

    except Training.DoesNotExist:
        return JsonResponse({'message': 'trainee does not exist'}, status=404)

    raw_query = 'CALL myupdate({});'.format(data['user_id'])
    results = executeSQL(raw_query)

    return JsonResponse({
        'message': 'success',
        'result': results,
    })


@csrf_exempt
@require_POST
def delete_training(request):
    data = json.loads(request.body)
    raw_query = """
        DELETE FROM Pokemon.public_info 
        WHERE user_id="{}" 
        AND training_id={};
    """.format(data['user_id'], data['training_id'])

    raw_query_2 = """
        DELETE FROM Pokemon.training_has_types WHERE training_id={}
    """.format(data['training_id'])

    try:
        executeSQLWrite(raw_query)
        executeSQLWrite(raw_query_2)
        training = Training.objects.get(training_id=data["training_id"])
        training.delete()

    except Training.DoesNotExist:
        return JsonResponse({'message': 'trainee does not exist'}, status=404)

    return JsonResponse({'message': 'success'})



