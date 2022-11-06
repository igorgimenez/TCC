from multiprocessing import context
from django.shortcuts import render, redirect  
from forum.forms import ForumForm, ComentarioForm, ReportarComentarioForm, ReportarTopicoForm
from forum.models import  Comentario, Forum, ReportarComentario, ReportarTopico
from django.contrib import messages
from datetime import datetime

def exibir(request):  
    forum = Forum.objects.all().filter(status=1)
    return render(request,"forum.html",{'forum':forum})  


def novo_topico(request):  
    return render(request,"novo_post.html") 


def criar(request):

    
    form = ForumForm()
    if request.method == "POST":  
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        autor = request.POST.get('autor')
        forum =  Forum(titulo=titulo, texto=texto, autor=autor,status=1)
        forum.save()
        context = {'form' : form} 
        messages.success(request, "Tópico criado com sucesso")
        return redirect("/forum")
    return redirect(request, 'novo_post.html', context)




def post(request, id):
    forum = Forum.objects.get(id=id)  
    comentario = Comentario.objects.filter(post_id=id).filter(status=1)
    return render(request,'visualizar_post.html', {'forum':forum, 'comentario':comentario})
    



def comentar(request):
    form = ComentarioForm()
    if request.method == "POST":  
        texto = request.POST.get('comentario')
        autor = request.POST.get('autor')
        post_id = request.POST.get('post_id')
        com =  Comentario(texto=texto, autor=autor,post_id=post_id,status='1')
        com.save()
        context = {'form' : form} 
        url_id= str(post_id)
        messages.success(request, "Comentário realizado com sucesso")      
        return redirect('/post/%s'%url_id)
    return render(request,'visualizar_post.html',context) 


def reportar_topico(request):
    form = ReportarTopicoForm()
    if request.method == "POST":  
        id_topico = request.POST.get('id_topico')
        report =  ReportarTopico(id_topico=id_topico,status='1')
        report.save()
        context = {'form' : form}
        messages.success(request, "Topico reportado com sucesso")
        return redirect ('/forum')    
    return render(request,'forum.html',context) 

def reportar_comentario(request):  
    form = ReportarComentarioForm()  
    if request.method == "POST":  
        id_comentario = request.POST.get('id_comentario')
        report =  ReportarComentario(id_comentario=id_comentario,status='1')
        report.save()
        context = {'form' : form}
        messages.success(request, "Comentario reportado com sucesso")
        return redirect ('/forum')    
    return render(request,'forum.html',context) 


