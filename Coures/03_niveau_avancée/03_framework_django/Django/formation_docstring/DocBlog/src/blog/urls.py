from django.urls import path
from .views import index ,article

urlpatterns = [
    path('', index) ,
    path('article_<str:numero_article>/',article) ,

]