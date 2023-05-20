from django.db import models
from datetime import datetime

# Create your models here.
class Sala(models.Model):
    nome = models.CharField(max_length=1000)
    class Meta:  
        db_table = "sala"  
class Mensagem(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    sala = models.CharField(max_length=1000000)
    class Meta:  
        db_table = "mensagem"