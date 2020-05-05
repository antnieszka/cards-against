# Generated by Django 3.0.5 on 2020-05-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("holes", models.PositiveIntegerField()),
            ],
            options={"verbose_name": "card", "verbose_name_plural": "cards",},
        ),
        migrations.CreateModel(
            name="Deck",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={"verbose_name": "deck", "verbose_name_plural": "decks",},
        ),
    ]
