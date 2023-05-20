
from django.shortcuts import render, redirect, HttpResponseRedirect
from autenticacao.forms import AutenticacaoForm

from autenticacao.models import Autenticacao
from django.contrib import messages
from datetime import datetime

def usuario(request):  
    return render(request,"usuario.html") 


def editar(request):  
     if 'user' not in request.session:
        return render(request,"usuario_google.html")
     else:
        sessao = request.session['user']
        usuario = Autenticacao.objects.get(usuario=sessao)  
        return render(request,'usuario.html', {'usuario':usuario})  

def editargoogle(request): 
    return render(request,'usuario_google.html', {'usuario':usuario})  

def salvarperfilgoogle(request):  
    sessao=request.user.email
    if Autenticacao.objects.filter(usuario=sessao).exists():
        form = AutenticacaoForm()
        if request.method == 'POST':    
            usuario = Autenticacao.objects.get(email=sessao)  
            usuario.nome = request.POST.get('nome')
            usuario.email=request.POST.get('email')
            usuario.telefone=request.POST.get('telefone')
            usuario.data_nascimento=request.POST.get('data_nascimento')
            usuario.usuario=request.POST.get('usuario')
            usuario.publico=request.POST.get('publico')
            usuario.updated_at = datetime.now()
            usuario.save(update_fields=['nome','email','usuario','publico','telefone','data_nascimento','updated_at'])
            context = {'form' : form} 
            messages.success(request, "Atualizado com sucesso")
            return render(request,'usuario_google.html') 
    else:
        form = AutenticacaoForm()
        if request.method == 'POST':
                    publico = request.POST.get('publico')
                    error_message = None
                    user = Autenticacao(nome=request.user.email, email=request.user.email, usuario=request.user.email,senha="123456",cpf="123456789",publico=publico,data_nascimento="01/01/2000",telefone="1111111111")
                    user.save()
                    messages.success(request, "Atualizado com sucesso")
         
    context = {'form' : form }  
    return render(request,'usuario_google.html',context)


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

