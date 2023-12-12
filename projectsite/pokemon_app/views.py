from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from pokemon_app.models import PokemonCard, Trainer, Collection
from pokemon_app.forms import TrainerForm

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

#Trainer CRUD

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')

#PokemonCard CRUD
class PokemonCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCard
    template_name = 'pokemon_card_add.html'
    success_url = reverse_lazy('pokemon-card')

class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCard
    template_name = 'pokemon_card_edit.html'
    success_url = reverse_lazy('pokemon-card')

class PokemonDeleteView(DeleteView):
    model = PokemonCard
    form_class = PokemonCard
    template_name = 'pokemon_card_del.html'
    success_url = reverse_lazy('pokemon-card')

    
# Create your views here.
