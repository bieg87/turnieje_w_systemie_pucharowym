from django.views.generic.edit import CreateView
from turnieje.forms.register_form import RegisterForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    success_message = "Twój profil został utworzony"
