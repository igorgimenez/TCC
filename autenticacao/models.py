from django.db import models 
from django.core.validators import MinLengthValidator

class Autenticacao(models.Model):  
    
    nome = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)  
    usuario = models.CharField(max_length=100)  
    senha = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    publico=models.CharField(max_length=20)
    telefone=models.CharField(max_length=20)
    data_nascimento=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:  
        db_table = "usuarios"  

    
    @staticmethod
    def get_user_by_usuario(usuario):
        try:
            return Autenticacao.objects.get(usuario=usuario)
        except:
            return False