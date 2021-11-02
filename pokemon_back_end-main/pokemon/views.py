import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from pokemon.models import Pokemon, Type, TypeRelation
from .serializers import PokemonSerializer, TypeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


def executeSQLRead(sql):
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
def get_pokemons(request):
    # get 5 pokemon
    pokemon = Pokemon.objects.order_by('-pokemon_id')[:20]
    data = PokemonSerializer(pokemon, many=True).data
    return JsonResponse(data, safe=False)


@require_GET
def get_types(request):
    types = Type.objects.all()
    data = TypeSerializer(types, many=True).data
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_POST
def search_pokemon_by_id(request):
    """
    Get 5 pokemon with id >= given data
    """
    data = json.loads(request.body)
    pokemon = Pokemon.objects.filter(pokemon_id__gte=data['pokemon_id'])[:10]
    results = PokemonSerializer(pokemon, many=True).data
    return JsonResponse(results, safe=False)


@require_GET
def get_type_statistics(request):
    """
    Advanced Query function
    """
    return JsonResponse(executeSQLRead(
        '''
            SELECT 
                strength.attacking_id, 
                strength.s as sharpness, 
                weakness.w as fragility
            FROM (
                SELECT attacking_id, sum(effectiveness) as s
                FROM typerelation
                GROUP BY attacking_id
            ) AS strength LEFT OUTER JOIN (
                SELECT against_id, sum(effectiveness) as w
                FROM typerelation
                GROUP BY against_id
            ) AS weakness ON strength.attacking_id = weakness.against_id
            ORDER BY sharpness DESC, fragility ASC;
        '''
    ), safe=False)


@csrf_exempt
@require_POST
def create_pokemon(request):
    """
    Create a pokemon with given data
    """
    pokemon_id = random.randint(1000000, 9999999)
    data = json.loads(request.body)
    pokemon = Pokemon(
        pokemon_id=pokemon_id,
        hp=data['hp'],
        attack=data['attack'],
        defense=data['defense'],
        specialAttack=data['specialAttack'],
        specialDefense=data['specialDefense'],
        speed=data['speed'],
        height=random.randint(20, 100),
        weight=random.randint(20, 100),
        gender=random.randint(20, 100),
        generation=random.randint(0, 10),
        legendary=random.randint(0, 1)
    )
    pokemon.save()

    # manually add pokemon types since django doesn't support composite key
    raw_query = "INSERT INTO pokemon_has_types VALUES "
    for t in data['types']:
        raw_query += '(%s, "%s"),' % (pokemon_id, t)
    raw_query = raw_query[:-1]
    raw_query += ';'

    executeSQLWrite(raw_query)
    return JsonResponse({'message': 'success'})


@csrf_exempt
@require_POST
def update_pokemon(request):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.get(pokemon_id=data["pokemon_id"])

        pokemon.hp = data["hp"]
        pokemon.attack = data["attack"]
        pokemon.defense = data["defense"]
        pokemon.specialAttack = data["specialAttack"]
        pokemon.specialDefense = data["specialDefense"]
        pokemon.speed = data["speed"]
        pokemon.save()

    except Pokemon.DoesNotExist:
        return JsonResponse({'message': 'pokemon does not exist'}, status=404)

    return JsonResponse({'message': 'success'})


@csrf_exempt
@require_POST
def delete_pokemon(request):
    try:
        data = json.loads(request.body)
        pokemon = Pokemon.objects.get(pokemon_id=data["pokemon_id"])
        pokemon.delete()

    except Pokemon.DoesNotExist:
        return JsonResponse({'message': 'pokemon does not exist'}, status=404)

    return JsonResponse({'message': 'success'})