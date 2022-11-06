from django.db import models


class Roteiro(models.Model):  
    dia= models.CharField(max_length=20)
    v_id = models.CharField(max_length=20)
    horario_inicial= models.TimeField()
    horario_final= models.TimeField()
    lugar = models.CharField(max_length=100)
    acao = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "roteiro"