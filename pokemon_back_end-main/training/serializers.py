from rest_framework import serializers
from .models import *


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['pokemon_id', 'training_id', 'hp_T', 'attack_T', 'defense_T',
                  'specialAttack_T', 'specialDefense_T', 'speed_T', 'height_T', 
                  'weight_T']