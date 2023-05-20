from django.contrib import admin  
from django.urls import path  
from comunidade import views  



urlpatterns = [  
    path('comunidade', views.comunidade),
    path('comunidade_viagens/<str:usuario>', views.comunidade_viagens),
]  