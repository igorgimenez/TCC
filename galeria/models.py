from django.db import models

class Galeria(models.Model):
    v_id = models.CharField(max_length=20)   
    nome = models.CharField(max_length=50) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
  
    class Meta:  
        db_table = "galeria"  


class FotoGaleria(models.Model):
    v_gal = models.CharField(max_length=20)   
    img = models.ImageField(upload_to = 'galeria/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "foto_galeria"  