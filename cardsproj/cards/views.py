from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class GameRoom(TemplateView):
    template_name = "room.html"
