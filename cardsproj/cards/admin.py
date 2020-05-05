from django.contrib import admin

from cardsproj.cards.models import Deck, Card


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
