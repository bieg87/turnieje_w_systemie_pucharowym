from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class DateTournamentForm(forms.Form):
    date_from = forms.DateTimeField(label="Od daty", required=True,
                                    widget=DateTimePickerInput(format='%Y-%m-%d %H:%M:%S'))
    date_to = forms.DateTimeField(label="Do daty", required=True,
                                  widget=DateTimePickerInput(format='%Y-%m-%d %H:%M:%S'))
