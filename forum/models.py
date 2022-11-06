from django.db import models


class Forum(models.Model):  
    
    titulo = models.CharField(max_length=200)  
    texto = models.CharField(max_length=500)  
    autor = models.CharField(max_length=100)  
    status = models.CharField(max_length=10) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    class Meta:  
        db_table = "forum"  



class Comentario(models.Model):  
    
    texto = models.CharField(max_length=500)  
    autor = models.CharField(max_length=100) 
    post_id = models.CharField(max_length=100)  
    status = models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True) 


    class Meta:  
        db_table = "comentario"  


class ReportarTopico(models.Model):  

    id_topico = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)  
    class Meta:  
        db_table = "reportar_topico"  


class ReportarComentario(models.Model):  

    id_comentario = models.CharField(max_length=100) 
    status = models.CharField(max_length=10)  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:  
        db_table = "reportar_comentario"  