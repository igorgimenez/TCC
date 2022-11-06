from django.contrib import admin  
from django.urls import path  
from autenticacao import views
from atividades.views import atividades



urlpatterns = [   
     path('login',views.login),
     path('cadastrar',views.cadastrar),
     path('logar', views.logar),
     path('logout', views.logout),
     path('viagem', atividades),
      
      
]  