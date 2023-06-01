from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nazwa użytkownika", max_length=254, required=True)
    email = forms.EmailField(max_length=254, required=True)
    day_of_birth = forms.CharField(label="Data urodzenia", max_length=254, required=True)
    password1 = forms.CharField(label='Hasło', widget=forms.PasswordInput, help_text='')
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput, help_text='')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'day_of_birth')
        help_texts = {
            'username': None,
            'email': None,
            'day_of_birth': None
        }