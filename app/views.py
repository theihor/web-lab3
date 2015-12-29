from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    games = [(g.id, g.name) for g in Game.objects.all()]
    print(games)
    return render (request,"app/index.html", {"games" : games})
    # return HttpResponse("Piece of shit.")

def game(request):
    game_id = request.GET.get('id')
    print("I'm HERE!!")
    info = {}
    g = Game.objects.get(id=game_id)
    info["game_name"] = g.name
    info["price"] = g.price
    info["release_date"] = str(g.release_date)
    info["developer"] = g.developer.name
    info["developer_email"] = g.developer.email
    return render (request,"app/game.html", info)
