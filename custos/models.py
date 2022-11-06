from django.db import models

class Custo(models.Model):  
    tipo= models.CharField(max_length=50)
    v_id = models.CharField(max_length=20)
    valor = models.CharField(max_length=50)  
    obs = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "custo"