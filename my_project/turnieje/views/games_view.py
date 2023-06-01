import math
import random
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from turnieje.models import Tournaments, Games
from turnieje.forms.player_form import GamesForm
from django.shortcuts import render
from turnieje.forms.games_update_form import GamesUpdateForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from turnieje.forms.games_tournament_form import TournamentSelectForm


class TournamentView(ListView):
    model = Games
    template = 'turnieje/games_select_tournament.html'

    def get_context_data(self, **kwargs):
        context = super(TournamentView, self).get_context_data(**kwargs)
        context['tournaments'] = Tournaments.objects.all()
        return context


class CreateGamesView(CreateView):
    model = Games
    form_class = GamesForm

    def random_player(self, form):
        # Metoda losowo przydzielająca graczy do turnieju
        t_id = Tournaments.objects.get(name=form.cleaned_data['tournament']).id
        n = Games.objects.filter(tournament_id=t_id).filter(round=1).count()
        is_saved = False
        a = Games.objects.filter(tournament_id=t_id).filter(round=1).filter(first_player__isnull=True).count()
        b = Games.objects.filter(tournament_id=t_id).filter(round=1).filter(second_player__isnull=True).count()
        max_players = Tournaments.objects.get(id=t_id).max_players
        print(n * 2 - a - b)
        print(max_players)
        if n * 2 - a - b >= max_players:
            return False
        else:
            while not is_saved:
                x = random.randint(1, n)
                y = random.randint(1, 2)
                if y == 1:
                    if Games.objects.filter(tournament_id=t_id).filter(nr=x).filter(first_player=None).exists():
                        Games.objects.filter(tournament_id=t_id).filter(nr=math.floor(x)).update(
                            first_player=form.cleaned_data['player'])
                        is_saved = True
                else:
                    if Games.objects.filter(tournament_id=t_id).filter(nr=x).filter(second_player=None).exists():
                        Games.objects.filter(tournament_id=t_id).filter(nr=x).update(
                            second_player=form.cleaned_data['player'])
                        is_saved = True
        return True

    def form_valid(self, form):
        result = self.random_player(form)
        if result:
            return render(self.request, 'turnieje/player_added.html')
        else:
            return render(self.request, 'turnieje/max_players.html')


class GamesUpdateView(UpdateView):
    model = Games
    form_class = GamesUpdateForm
    success_url = reverse_lazy('games_show')

    def fill_games(self, form):
        #automatyczne wypełnianie tabeli gier
        t_id = Tournaments.objects.get(name=form.cleaned_data['tournament']).id
        round_count = 0

        for i in range(1, form.cleaned_data['round'] + 1):
            round_count = round_count + Games.objects.filter(tournament=t_id, round=i).count()

        last_round_count = Games.objects.filter(tournament=t_id, round=form.cleaned_data['round']).count()
        game_number = round_count + math.ceil((form.cleaned_data['nr'] - round_count + last_round_count) / 2)
        if_next_round_exists = Games.objects.filter(tournament=t_id, round=int(form.cleaned_data['round']) + 1).exists()

        if int(form.cleaned_data['nr']) % 2 == 1 and if_next_round_exists:
            if int(form.cleaned_data['first_player_score']) > int(form.cleaned_data['second_player_score']):
                Games.objects.filter(tournament_id=t_id).filter(nr=game_number).update(
                    first_player=form.cleaned_data['first_player'])
            else:
                Games.objects.filter(tournament_id=t_id).filter(nr=game_number).update(
                    first_player=form.cleaned_data['second_player'])
        else:
            if int(form.cleaned_data['first_player_score']) > int(form.cleaned_data['second_player_score']):
                Games.objects.filter(tournament_id=t_id).filter(nr=game_number).update(
                    second_player=form.cleaned_data['first_player'])
            else:
                Games.objects.filter(tournament_id=t_id).filter(nr=game_number).update(
                    second_player=form.cleaned_data['second_player'])

    def form_valid(self, form):
        self.fill_games(form)
        response = super(GamesUpdateView, self).form_valid(form)
        return response


def get_games(request):
    if request.method == 'POST':
        form = TournamentSelectForm(request.POST)

        if form.is_valid():
            tournament_games = Games.objects.filter(tournament=request.POST['tournament'])
            return render(request, 'turnieje/games_tournament.html', {'form': form, 'tournament_games': tournament_games})

    else:
        form = TournamentSelectForm()

    return render(request, 'turnieje/games_tournament.html', {'form': form})
