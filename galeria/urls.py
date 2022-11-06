from django.contrib import admin  
from django.urls import path  
from galeria import views  



urlpatterns = [  
    path('galerias', views.galerias),
    path('nova_galeria/<int:id>', views.nova_galeria),
    path('criargaleria', views.criargaleria),
    path('editargaleria/<int:id>', views.editar),
    path('updategaleria/<int:id>', views.update), 
    path('excluirgaleria/<int:id>', views.excluir),
    path('fotos_galeria/<int:id>', views.fotos_galeria),
    path('adicionar_fotosgaleria/<int:id>', views.adicionar_fotosgaleria),
    path('criar_fotogaleria', views.criar_fotogaleria),

    
]  
