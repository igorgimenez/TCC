from django.contrib import admin  
from django.urls import path  
from viagem import views  
from atividades.views import atividades
from roteiros.views import roteiros
from custos.views import custos
from galeria.views import galerias


urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('nova_viagem', views.nova_viagem),  
    path('criarviagem', views.criar),
    path('viagens',views.exibir),  
    path('editarviagem/<int:id>', views.editar),  
    path('update/<int:id>', views.update),  
    path('excluirviagem/<int:id>', views.excluir),  
    path('atividades/<int:id>', atividades),  
    path('roteiros/<int:id>', roteiros),
    path('custos/<int:id>', custos),
    path('galerias/<int:id>', galerias),        
]  