from django.shortcuts import render, redirect, HttpResponseRedirect
from forum.models import  ReportarTopico, ReportarComentario ,Forum, Comentario
from forum.forms import ReportarTopicoForm
from django.contrib import messages



def adm(request):
    return render(request,"adm.html") 

def reportados(request):  

    topicos_reportados = ReportarTopico.objects.all().values('id_topico').distinct().filter(status = '1')
    topicos = Forum.objects.filter(pk__in=[topicos_reportados])

    comentarios_reportados = ReportarComentario.objects.all().values('id_comentario').distinct().filter(status = '1')
    comentarios = Comentario.objects.filter(pk__in=[comentarios_reportados])
    return render(request,"analise_reportados.html",{'topicos':topicos,'comentarios':comentarios})  


def excluir_topico(request, id):  
    forum = Forum.objects.get(id=id)  
    forum.status = '0'
    forum.save(update_fields=['status']) 
    ReportarTopico.objects.all().filter(id_topico = id).update(status='0') 
    messages.success(request, "Tópico excluido com sucesso")
    return redirect("/reports")  

def ignorar_topico(request, id):
    ReportarTopico.objects.all().filter(id_topico = id).update(status='0')
    messages.success(request, "Report de tópico ignorado com sucesso")
    return redirect("/reports") 


def excluir_comentario(request, id):  
    comentario = Comentario.objects.get(id=id)  
    comentario.status = '0'
    comentario.save(update_fields=['status']) 
    ReportarComentario.objects.all().filter(id_comentario = id).update(status='0') 
    messages.success(request, "Comentário excluido com sucesso")
    return redirect("/reports")  

def ignorar_comentario(request, id):
    ReportarComentario.objects.all().filter(id_comentario = id).update(status='0')
    messages.success(request, "Report de comentário ignorado com sucesso")
    return redirect("/reports") 