from django.db import models

class Training(models.Model):

    class Meta:
        db_table = 'training'

    pokemon_id = models.IntegerField(null=True)
    training_id = models.AutoField(primary_key=True)
    hp_T = models.IntegerField(null=True)
    attack_T = models.IntegerField(null=True)
    defense_T = models.IntegerField(null=True)
    specialAttack_T = models.IntegerField(null=True)
    specialDefense_T = models.IntegerField(null=True)
    speed_T = models.IntegerField(null=True)
    height_T = models.IntegerField(null=True)
    weight_T = models.IntegerField(null=True)
    
