import math

from django.views.generic import ListView, FormView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from turnieje.models import Tournaments, Games
from turnieje.forms.turnieje_form import TournamentsForm
from turnieje.forms.date_tournaments_form import DateTournamentForm
from django.shortcuts import render, HttpResponseRedirect


class CreateTournamentView(SuccessMessageMixin, CreateView):
    model = Tournaments
    form_class = TournamentsForm
    success_message = "Turniej został zapisany"
    success_url = reverse_lazy('all_tournaments')

    def create_games(self, form, tournament_id):
        # obliczanie numeracji meczów, rund oraz zapis do bazy wymaganej ilości rozgrywek
        n = form.cleaned_data['max_players'] / 2 if math.log(form.cleaned_data['max_players'],
                                                             2).is_integer() else math.pow(2, math.ceil(
                                                                    math.log(form.cleaned_data['max_players'], 2)) - 1)
        t = Tournaments.objects.get(id=tournament_id)
        k = 1
        for j in range(int(math.log(int(n), 2)) + 1):
            for i in range(int(n)):
                e = Games(tournament=t, round=j + 1, nr=k)
                e.save(force_insert=True)
                k = k + 1
            n = n / 2

    def form_valid(self, form):
        obj = form.save()
        self.create_games(form, obj.id)
        response = super(CreateTournamentView, self).form_valid(form)
        return response


class AllTournamentsView(ListView):
    model = Tournaments


class DeleteTournamentView(SuccessMessageMixin, DeleteView):
    model = Tournaments
    success_url = reverse_lazy('all_tournaments')
    success_message = "Turniej został usunięty"


class UpdateTournamentView(SuccessMessageMixin, UpdateView):
    model = Tournaments
    success_url = reverse_lazy('all_tournaments')
    form_class = TournamentsForm
    success_message = "Turniej został zaktualizowany"


def get_tournament_dates(request):
    if request.method == 'POST':
        form = DateTournamentForm(request.POST)

        if form.is_valid():
            tournaments = Tournaments.objects.filter(date_of_start__gte=request.POST['date_from'],
                                                     date_of_start__lte=request.POST['date_to']).order_by(
                                                                                                        'date_of_start')
            return render(request, 'turnieje/date_tournaments.html', {'form': form, 'tournaments': tournaments})

    else:
        form = DateTournamentForm()

    return render(request, 'turnieje/date_tournaments.html', {'form': form})
