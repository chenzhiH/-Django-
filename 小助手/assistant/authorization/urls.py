from django.shortcuts import render
from django.urls import path
# Create your views here.
from . import views
urlpatterns = [
    path('test',views.test_session),
    #path('test2',views.test_session2),
    path('status', views.get_status, name='get_status'),
    path('user',views.UserView.as_view()),
    path('logout', views.logout, name='logout'),
    path('authorize', views.authorize, name='authorize')
]