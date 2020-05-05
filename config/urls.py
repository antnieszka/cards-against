"""cardsproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, re_path

from cardsproj.cards import views as cards_views, api_views
from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", cards_views.IndexView.as_view()),
    path("rooms/", cards_views.GameRoom.as_view(), name='game_room'),
    path("api/decks", api_views.list_decks),
    path("api/cards/<str:deck_name>", api_views.list_cards_for_deck),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", serve),
    ]
