from django.db import models
from django.urls import reverse


class Tournaments(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    date_of_start = models.DateTimeField()
    max_players = models.IntegerField()

    def __str__(self):
        return str(self.name)
