from django.contrib import admin  
from django.urls import path  
from atividades import views  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('atividades', views.atividades),
    path('nova_atividade/<int:id>', views.nova_atividade),
    path('criar', views.criar),
    path('editaratividade/<int:id>', views.editar),
    path('updateatividade/<int:id>', views.update), 
    path('excluiratividade/<int:id>', views.excluir),
]  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)