from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'turnieje/index.html'


class GreetingsView(TemplateView):
    template_name = 'turnieje/greetings.html'