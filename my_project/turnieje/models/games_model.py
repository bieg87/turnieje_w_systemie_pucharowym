from django.db import models

from turnieje.models import Tournaments


class Games(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    tournament = models.ForeignKey(Tournaments, on_delete=models.CASCADE)
    round = models.IntegerField(null=True)
    first_player = models.CharField(max_length=50, null=True)
    first_player_score = models.IntegerField(null=True)
    second_player = models.CharField(max_length=50, null=True)
    second_player_score = models.IntegerField(null=True)
    nr = models.IntegerField(null=True)


