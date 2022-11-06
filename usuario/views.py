
from django.shortcuts import render, redirect, HttpResponseRedirect
from autenticacao.forms import AutenticacaoForm

from autenticacao.models import Autenticacao
from django.contrib import messages
from datetime import datetime

def usuario(request):  
    return render(request,"usuario.html") 


def editar(request):  
    sessao = request.session['user']
    usuario = Autenticacao.objects.get(usuario=sessao)  
    return render(request,'usuario.html', {'usuario':usuario})  


def update_usuario(request, id): 
    form = AutenticacaoForm()
    if request.method == 'POST': 
        usuario = Autenticacao.objects.get(id=id)  
        usuario.nome = request.POST.get('nome')
        usuario.email=request.POST.get('email')
        usuario.telefone=request.POST.get('telefone')
        usuario.data_nascimento=request.POST.get('data_nascimento')
        usuario.usuario=request.POST.get('usuario')
        usuario.publico=request.POST.get('publico')
        usuario.updated_at = datetime.now()
        usuario.save(update_fields=['nome','email','usuario','publico','telefone','data_nascimento','updated_at'])
        context = {'form' : form} 
        messages.success(request, "Usuario atualizado com sucesso")
        return redirect("/usuario")
    return redirect(request, 'usuario.html', context)

