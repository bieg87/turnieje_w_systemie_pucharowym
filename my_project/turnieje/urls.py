from django.urls import path
from turnieje.views import *
from django.contrib.auth import views as auth_views
from turnieje.views.register_view import RegisterView
from turnieje.views.turnieje_view import *
from turnieje.views.games_view import *
from . import views
from .views.index_view import GreetingsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('tournaments', AllTournamentsView.as_view(), name="all_tournaments"),
    path('tournaments/add', CreateTournamentView.as_view(), name="tournament_add"),
    path('tournaments/<int:pk>/delete', DeleteTournamentView.as_view(), name="tournament_delete"),
    path('tournaments/<int:pk>/update', UpdateTournamentView.as_view(), name="tournament_update"),
    path('games/add', CreateGamesView.as_view(), name="games_add"),
    path('games/<int:pk>/update', GamesUpdateView.as_view(), name="games_update"),
    path('tournaments/date_tournaments/', views.turnieje_view.get_tournament_dates, name="date_tournaments"),
    path('games/', views.games_view.get_games, name="games_show"),
    path('greetings/', GreetingsView.as_view(), name='greetings'),
]
