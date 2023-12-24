from django.shortcuts import render


from .models import Band 

from django.http import HttpResponse


def notre_base(request):
    

    return render(request,"listings/donnée.html")


def hello(request):
    base = Band.objects.all()
    return render(request , "listings/hello.html" , context={"base":base})








