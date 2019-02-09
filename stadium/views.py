from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import Team,Player,Stadium,Position

#CRUD TEAM

class TeamList(ListView):
    model = Team

class TeamView(DetailView):
    model = Team

class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'stadium_id']
    success_url = reverse_lazy('team_list')

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'stadium_id']
    success_url = reverse_lazy('team_list')

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('team_list')

#CRUD STADIUM

class StadiumList(ListView):
    model = Stadium

class StadiumView(DetailView):
    model = Stadium

class StadiumCreate(CreateView):
    model = Stadium
    fields = ['name']
    success_url = reverse_lazy('stadium_list')

class StadiumUpdate(UpdateView):
    model = Stadium
    fields = ['name']
    success_url = reverse_lazy('stadium_list')

class StadiumDelete(DeleteView):
    model = Stadium
    success_url = reverse_lazy('stadium_list')

#CRUD POSITION

class PositionList(ListView):
    model = Position

class PositionView(DetailView):
    model = Position

class PositionCreate(CreateView):
    model = Position
    fields = ['name']
    success_url = reverse_lazy('position_list')

class PositionUpdate(UpdateView):
    model = Position
    fields = ['name']
    success_url = reverse_lazy('position_list')

class PositionDelete(DeleteView):
    model = Position
    success_url = reverse_lazy('position_list')

# CRUD PLAYER

class PlayerList(ListView):
    model = Player

class PlayerView(DetailView):
    model = Player

class PlayerCreate(CreateView):
    model = Player
    fields = ['name','position_id','number','team_id']
    success_url = reverse_lazy('player_list')

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name','position_id','number','team_id']
    success_url = reverse_lazy('player_list')

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('player_list')