from django.contrib import admin  
from django.urls import path  
from administracao import views



urlpatterns = [
 path('adm',views.adm),     
 path('reports',views.reportados),
 path('excluirtopico/<int:id>', views.excluir_topico),
 path('ignorartopico/<int:id>', views.ignorar_topico),
 path('excluircomentario/<int:id>', views.excluir_comentario),
 path('ignorarcomentario/<int:id>', views.ignorar_comentario),
]  