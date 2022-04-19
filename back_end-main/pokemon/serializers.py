from rest_framework import serializers
from .models import *


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id']


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['pokemon_id', 'hp', 'attack', 'defense', 'specialAttack',
                  'specialDefense', 'speed', 'height', 'weight', 'gender',
                  'generation', 'legendary', 'types']
