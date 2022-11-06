from django.db import models  
import datetime


class Atividade(models.Model):
    v_id = models.CharField(max_length=20)   
    duracao = models.CharField(max_length=20)  
    lugar = models.CharField(max_length=100)
    obs =  models.CharField(max_length=100)
    img = models.ImageField(upload_to = 'images/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:  
        db_table = "atividade"  