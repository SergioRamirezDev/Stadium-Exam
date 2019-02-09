"""stadium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('stadium', views.StadiumList.as_view(), name='stadium_list'),
    path('stadium/view/<int:pk>', views.StadiumView.as_view(), name='stadium_view'),
    path('stadium/new', views.StadiumCreate.as_view(), name='stadium_new'),
    path('stadium/view/<int:pk>', views.StadiumView.as_view(), name='stadium_view'),
    path('stadium/edit/<int:pk>', views.StadiumUpdate.as_view(), name='stadium_edit'),
    path('stadium/delete/<int:pk>', views.StadiumDelete.as_view(), name='stadium_delete'),

    path('team', views.TeamList.as_view(), name='team_list'),
    path('team/view/<int:pk>', views.TeamView.as_view(), name='team_view'),
    path('team/new', views.TeamCreate.as_view(), name='team_new'),
    path('team/view/<int:pk>', views.TeamView.as_view(), name='team_view'),
    path('team/edit/<int:pk>', views.TeamUpdate.as_view(), name='team_edit'),
    path('team/delete/<int:pk>', views.TeamDelete.as_view(), name='team_delete'),

    path('position', views.PositionList.as_view(), name='position_list'),
    path('position/view/<int:pk>', views.PositionView.as_view(), name='position_view'),
    path('position/new', views.PositionCreate.as_view(), name='position_new'),
    path('position/view/<int:pk>', views.PositionView.as_view(), name='position_view'),
    path('position/edit/<int:pk>', views.PositionUpdate.as_view(), name='position_edit'),
    path('position/delete/<int:pk>', views.PositionDelete.as_view(), name='position_delete'),

    path('player', views.PlayerList.as_view(), name='player_list'),
    path('player/view/<int:pk>', views.PlayerView.as_view(), name='player_view'),
    path('player/new', views.PlayerCreate.as_view(), name='player_new'),
    path('player/view/<int:pk>', views.PlayerView.as_view(), name='player_view'),
    path('player/edit/<int:pk>', views.PlayerUpdate.as_view(), name='player_edit'),
    path('player/delete/<int:pk>', views.PlayerDelete.as_view(), name='player_delete'),

]
