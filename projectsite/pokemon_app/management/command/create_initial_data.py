from typing import Any
from django.core.management.base import BaseCommand
from pokemon_app.models import PokemonCard, Trainer

class Command(BaseCommand):
    help = 'Create initial data for the application' # <-- descrition of the command 

    def handle(self, *args, **kwargs):
        self.create_pokemon_cards() #<-- where logic is implemented
        #self.create_trainers()

    def create_pokemon_cards(self):
        #create pokemon cards instances
        cardl = PokemonCard(name="Pikachu",  rarity="Rare", hp=60,
                            card_type="Electric", attack="Thunder Shock", description="A mouse-like pokemon that can generate electricity.",
                            weakness="Ground", card_number=25, release_date="1999=01-09", evolution_stage="Basic", abilities="Static")
        cardl = PokemonCard("Pikachu", "Rare", 60, ["Electric"], "Thunder Shock", "A mouse-like pokemon that can generate electricity.",
                            ["Ground"], 25, "Basic", ["Static"])
        
        cardl.save()#<--- save card1 to Pokemon Table
        self.stdout.write(self.style.SUCCESS('Succesfully Created Pokemon cards.')) #<-- display success message

    def create_trainers(self):
        pass