from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from pokemon_app.models import PokemonCard, Trainer, Collection
from pokemon_app.forms import TrainerForm, PokemonCardForm, CollectionForm 

from django.urls import reverse_lazy

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
    context_object_name = 'pokemoncard-list'
    template_name = 'pokemon-card.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class Collection(ListView):
    model = Collection
    context_object_name = 'collection-list'
    template_name = 'collection.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

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

#PokemonCard CRUD
class PokemonCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'add.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'edit.html'
    success_url = reverse_lazy('pokemoncard-list')

class PokemonDeleteView(DeleteView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'del.html'
    success_url = reverse_lazy('pokemoncard-list')

#Collection CRUD
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
    form_class = CollectionForm 
    template_name = 'del.html'
    success_url = reverse_lazy('collection-list')

    
# Create your views here.
