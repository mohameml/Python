from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1> Bonjour , Bienvenue sur mon site </h1>")


def index_2(request):
    return render(request,"exemple.html")
