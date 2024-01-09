from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from pokemon_app.models import PokemonCard, Trainer, Collection
from pokemon_app.forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy
import json

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
    paginate_by = 5


    
class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection '
    template_name = 'collection.html'
    paginate_by = 5

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemon-cards.html"
    json_file_path = 'data\pokemon_data.json'
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
        
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])


#Trainer CRUD
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'add.html'
    success_url = reverse_lazy('trainer-list') 

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'edit.html'
    success_url = reverse_lazy('trainer-list')   

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'del.html'
    success_url = reverse_lazy('trainer-list')

#pokemon CRUD
class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'add.html'
    success_url = reverse_lazy('pokemoncard-list')
    
class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'edit.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'del.html'
    success_url = reverse_lazy('pokemoncard-list')

#collection CRUD

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'add.html'
    success_url = reverse_lazy('collection-list')
    
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'edit.html'
    success_url = reverse_lazy('collection-list')
    
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'del.html'
    success_url = reverse_lazy('collection-list')
    
# Create your views here.