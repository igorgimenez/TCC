from django.contrib import admin  
from django.urls import path  
from custos import views



urlpatterns = [  
 path('custos/<int:id>', views.custos),
 path('criar_custo/<int:id>',views.criar_custo),
 path('editarcusto/<int:id>', views.editar),
 path('update_custo/<int:id>', views.update_custo),  
 path('excluir_custo/<int:id>', views.excluir), 
 path('custo_grafico/<int:id>',views.pie_chart),
 path('exportar/<int:id>',views.exportar),
 
]  