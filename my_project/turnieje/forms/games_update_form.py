from django import forms
from turnieje.models import Games
from django.forms import ModelForm


class GamesUpdateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(GamesUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_player'].required = False
        self.fields['second_player'].required = False
        self.fields['second_player'].disabled = True
        self.fields['first_player'].disabled = True

    class Meta:
        model = Games
        template = 'turnieje/games_update_form.html'
        fields = ['tournament', 'first_player', 'second_player', 'first_player_score', 'second_player_score', 'nr', 'round']
        labels = {
            'first_player': 'Pierwszy gracz:',
            'second_player': 'Drugi gracz:',
            'first_player_score': 'Punkty pierwszego gracza:',
            'second_player_score': 'Punkty drugiego gracza:'
        }
        widgets = {
            'tournament': forms.HiddenInput(),
            'nr': forms.HiddenInput(),
            'round': forms.HiddenInput()
        }
