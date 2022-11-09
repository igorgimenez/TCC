from importlib.metadata import requires
from django.shortcuts import render, redirect, HttpResponseRedirect
from autenticacao.forms import AutenticacaoForm  
from autenticacao.models import  Autenticacao  
from django.contrib.auth.hashers import make_password, check_password
from django.views import  View
from viagem.models import  Viagem
from custos.models import Custo
from forum.models import Forum, Comentario
from atividades.models import Atividade
from galeria.models import Galeria, FotoGaleria
from roteiros.models import Roteiro
from django.db.models import Sum
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie



def login(request):  
    return render(request,"login.html") 


def cadastrar(request):  
    
    form = AutenticacaoForm()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario')
        senha  = request.POST.get('senha')
        senha = make_password(senha)
        cpf  = request.POST.get('cpf')
        publico = request.POST.get('publico')
        telefone = request.POST.get('telefone')
        data_nascimento=request.POST.get('data_nascimento')
        error_message = None
        
        if Autenticacao.objects.filter(usuario=usuario).exists():
            error_message = 'Usuário já existe'
            return render(request,'cadastrar.html',{'error': error_message}) 
        else:
            user = Autenticacao(nome=nome, email=email, usuario=usuario,senha=senha,cpf=cpf,publico=publico,data_nascimento=data_nascimento,telefone=telefone)
            user.save()
            messages.success(request, "Usuário criado com sucesso")
        return redirect("/login")  
    context = {'form' : form }  
    return render(request,'cadastrar.html',context) 


@csrf_protect
@ensure_csrf_cookie  
def logar(request):
    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = Autenticacao.get_user_by_usuario(usuario)
        uid= Autenticacao.get_user_by_usuario(id)
        error_message = None
        if user:
            flag = check_password(senha, user.senha)
            if flag:
                if usuario == 'administrador':
                    request.session['user'] = usuario
                    return redirect("/adm") 
                else:
                    request.session['user'] = usuario
                    return redirect("/home") 
            else:
                error_message = 'Usuário ou Senha incorretos'
                
        else:
            error_message = 'Usuário ou Senha incorretos'
        
        print(usuario, senha)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    del request.session['user']
    return render(request,'login.html')


 