"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from pokemon_app.views import HomePageView, TrainerList, PokemonCard, Collection, TrainerCreateView, TrainerUpdateView, TrainerDeleteView, PokemonCreateView, PokemonUpdateView, PokemonDeleteView
from pokemon_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete',TrainerDeleteView.as_view(), name='trainer-delete'),
    
    path('pokemon-card', PokemonCard.as_view(), name='pokemon-card'),
    path('pokemon-card/add', PokemonCreateView.as_view(), name='pokemon-add'),
    path('pokemon-card/<pk>', PokemonUpdateView.as_view(), name='pokemon-update'),
    path('pokemon-card/<pk>/delete', PokemonDeleteView.as_view(), name='pokemon-delete'),
    path('collection', Collection.as_view(), name='collection'),
]
