from django.shortcuts import render


# Create your views here.
#from django.http import HttpResponse


def index(request):
    return render(request,"index.html")

def FAQ(request):
    return render(request,"FAQ.html")

def about(request):
    return render(request,"about.html")

def game(request):
    return render(request,"game.html")

def event(request):
    return render(request,"event.html")

def tournament(request):
    return render(request,"tournament.html")

def athletics(request):
    return render(request,"athletics.html")

def badminton(request):
    return render(request,"badminton.html")

def basketball(request):
    return render(request,"basketball.html")


def chess(request):
    return render(request,"chess.html")


def cricket(request):
    return render(request,"cricket.html")


def football(request):
    return render(request,"football.html")


def handball(request):
    return render(request,"handball.html")

def volleyball(request):
    return render(request,"volleyball.html")


def hockey(request):
    return render(request,"hockey.html")




