from django import forms
from django.forms import ModelForm
from turnieje.models import Games


class TournamentSelectForm(ModelForm):

    class Meta:
        model = Games
        fields = ['tournament']
        labels = {
            'tournament': 'Wybierz turniej'
        }
