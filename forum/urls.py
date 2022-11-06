from django.contrib import admin  
from django.urls import path  
from forum import views  


urlpatterns = [  
   
    path('forum',views.exibir),
    path('novo_topico',views.novo_topico),
    path('criar_topico',views.criar),
    path('post/<int:id>', views.post),
    path('comentar',views.comentar),
    path('reportar_topico',views.reportar_topico),
    path('reportar_comentario',views.reportar_comentario),
]  