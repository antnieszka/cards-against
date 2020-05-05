from django.http import JsonResponse

from cardsproj.cards.models import Deck, Card


def list_decks(request):
    decks = Deck.objects.values_list("name", flat=True)

    return JsonResponse(list(decks), safe=False)


def list_cards_for_deck(request, deck_name):
    cards = Card.objects.filter(deck__name=deck_name).values("text", "holes")

    return JsonResponse(list(cards), safe=False)