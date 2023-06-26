from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1> Hello Django ! </h1>')

def about_us(request) :

    chaine = """<h1> A bout us </h1>
    <p> Bonjour nous sommes heureux de partagér avce vous 
    notre expérience dans le domaine de dévelloppemnet <br>
    !!!!!
    N'hésiter pas de poser de questions 
    ciao 
    <p>
    """

    return HttpResponse(chaine)

