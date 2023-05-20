from django.urls import path
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),
    path('<str:sala>/', views.sala, name='sala'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('BuscaMensagem/<str:sala>/', views.BuscaMensagem, name='BuscaMensagem'),
]