from django.contrib import admin
# Register your models here.
from .models import PokemonCard, Collection, Trainer

# admin.site.register(PokemonCard)

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "cardtype", "attack",
                    "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities")
    search_fields = ("name",)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "trainer", "collection_date")
    search_fields = ("name",)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email")
    search_fields = ("name",)