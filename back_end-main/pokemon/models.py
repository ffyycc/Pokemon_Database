from django.db import models

# Create your models here.
class Type(models.Model):

    class Meta:
        db_table = 'type'
    id = models.CharField(primary_key=True, max_length=30, null=False)

class TypeRelation(models.Model):

    class Meta:
        db_table = 'typerelation'

    attacking_id = models.ManyToManyField(Type, related_name='types_attacking')
    against_id = models.ManyToManyField(Type, related_name='types_against')
    effectiveness = models.FloatField(null=False)


class Pokemon(models.Model):

    class Meta:
        db_table = 'pokemon'

    # use MYSQL table as references
    pokemon_id = models.AutoField(primary_key=True)
    hp = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    specialAttack = models.IntegerField(null=True)
    specialDefense = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    gender = models.IntegerField(null=True)
    generation = models.IntegerField(null=True)
    legendary = models.BooleanField(null=True)
    types = models.ManyToManyField(
        Type, db_table='pokemon_has_types')