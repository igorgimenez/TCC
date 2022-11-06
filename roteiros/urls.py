from django.contrib import admin  
from django.urls import path  
from roteiros import views



urlpatterns = [  
 path('criar_roteiros/<int:id>',views.criar_roteiros),
 path('roteiros', views.roteiros),
 path('editaroteiro/<int:id>', views.editar),
 path('update_roteiro/<int:id>', views.update_roteiro),  
 path('excluir_roteiro/<int:id>', views.excluir), 
 path('pdf/<int:id>/', views.render_pdf),
 path('pdf_filtro/<int:id>/<int:dia>/', views.render_pdf_filtro),
]  