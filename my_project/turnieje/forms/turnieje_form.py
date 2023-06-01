from django.forms import ModelForm
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from turnieje.models import Tournaments


class TournamentsForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = ['name', 'date_of_start', 'max_players']
        labels = {
            "name": "Nazwa turnieju:",
            "date_of_start": "Data rozpoczęcia turnieju:",
            "max_players": "Maksymalna liczba graczy:"
        }
        widgets = {
            'date_of_start': DateTimePickerInput(format='%Y-%m-%d %H:%M:%S')
        }
