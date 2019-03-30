from django.shortcuts import render
from .view import weather,menu,server
from django.urls import path
# Create your views here.

urlpatterns = [
    path('menu',menu.get_menu),
    path('weather',weather.weatherView.as_view()),
    path('stock',server.stock),
    path('constellation',server.constellation),
    path('joke',server.joke),
]
