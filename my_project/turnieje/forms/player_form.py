from django import forms
from turnieje.models import Games
from django.forms import ModelForm


class GamesForm(ModelForm):
    player = forms.CharField(label="Nazwa gracza:")

    class Meta:
        model = Games
        fields = ['tournament']
        labels = {
            "tournament": "Nazwa turnieju:",
        }
