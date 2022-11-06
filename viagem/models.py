from django.db import models  

class Viagem(models.Model):  
    duracao = models.CharField(max_length=20)  
    lugar = models.CharField(max_length=100)
    usuario= models.CharField(max_length=200) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "viagem"  