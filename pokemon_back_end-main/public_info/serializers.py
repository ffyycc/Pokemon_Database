from rest_framework import serializers
from .models import *


# class TypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Type
#         fields = ['id']

class PublicinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicinfo
        fields = ['user_id','training_id','share_info']


# class PokemonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pokemon
#         fields = ['pokemon_id', 'hp', 'attack', 'defense', 'specialAttack',
#                   'specialDefense', 'speed', 'height', 'weight', 'gender',
#                   'generation', 'legendary', 'types']


