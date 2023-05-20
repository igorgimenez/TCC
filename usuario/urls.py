from django.contrib import admin  
from django.urls import path  
from usuario import views



urlpatterns = [  
 path('usuario',views.editar),
 path('usuariogoogle',views.editargoogle),
 path('update_usuario/<int:id>', views.update_usuario),
 path('update_google', views.salvarperfilgoogle),
]  