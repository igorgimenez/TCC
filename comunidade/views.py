from django.shortcuts import render,redirect

from autenticacao.models import Autenticacao
from chat.models import Sala
from viagem.models import  Viagem 

def comunidade(request): 
    if 'user' not in request.session:  
        sessao = request.user.email
        usuario = Autenticacao.objects.exclude(usuario=sessao).exclude(usuario='').filter(publico="Publico")
        sala = Sala.objects.filter(nome__icontains=sessao)
        return render(request,"comunidade.html",{'usuario':usuario,'sala':sala})  
    else:
        sessao = request.session['user']
        usuario = Autenticacao.objects.exclude(usuario=sessao).exclude(usuario='').filter(publico="Publico")
        sala = Sala.objects.filter(nome__icontains=sessao)
        return render(request,"comunidade.html",{'usuario':usuario,'sala':sala})
 

def comunidade_viagens(request,usuario):
    viagens = Viagem.objects.filter(usuario=usuario)
    return render(request,"viagem_comunidade.html",{'viagens':viagens}) 
