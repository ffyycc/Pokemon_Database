from django.db import models

class Publicinfo(models.Model):

    class Meta:
        db_table = 'public_info'
        unique_together = (("user_id", "training_id"),)

    user_id = models.TextField(null=False)
    training_id = models.IntegerField(null=False)
    share_info = models.BooleanField(null=True)