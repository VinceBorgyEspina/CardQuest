from django.shortcuts import render
from django.views.generic.list import ListView
from pokemon_app.models import PokemonCard, Trainer, Collection

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer 
    context_object_name = 'trainer'
    template_name = "trainers.html"
    paginate_by = 15

class PokemonCard(ListView):
    model = PokemonCard
    context_object_name = 'pokemon card'
    template_name = 'pokemon-card.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class Collection(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
# Create your views here.
