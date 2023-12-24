from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    date = datetime.today()
    my_dict = {"date":date}
    return render(request,"DocBlog/index.html" , context =my_dict)


