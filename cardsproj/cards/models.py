from django.contrib.auth import get_user_model
from django.db import models


class Deck(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(to=get_user_model(), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "deck"
        verbose_name_plural = "decks"

    def __str__(self):
        return self.name


class Card(models.Model):
    text = models.TextField()
    holes = models.PositiveIntegerField()
    deck = models.ManyToManyField(to=Deck)

    class Meta:
        verbose_name = "card"
        verbose_name_plural = "cards"

    def __str__(self):
        return f"{self.text[:50]}"
