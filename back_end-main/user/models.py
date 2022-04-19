from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'user'
    
    # use MYSQL table as references
    user_id = models.TextField(primary_key=True)
    userName = models.TextField(null = True)
    userPassword = models.TextField(null = True)
    userEmail = models.TextField(null = True)
    privacy = models.IntegerField(null = True)
    