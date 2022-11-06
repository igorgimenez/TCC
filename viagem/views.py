from django.shortcuts import render, redirect  
from viagem.forms import ViagemForm  
from viagem.models import  Viagem  
from django.contrib import messages
from datetime import datetime

def nova_viagem(request):  

    context ={}
  
    form = ViagemForm(request.POST or None)
  
    context['form']= form
    return render(request, "criar_viagem.html", context)
    

def criar(request):

    
    form = ViagemForm()
    if request.method == "POST":  
        duracao = request.POST.get('duracao')
        lugar = request.POST.get('lugar')
        usuario = request.POST.get('usuario')
        viagem = Viagem(duracao=duracao, lugar=lugar, usuario=usuario)
        viagem.save()
    context = {'form' : form}    
    messages.success(request, "Viagem criada com sucesso")
    return redirect ('/viagens') 
    



def exibir(request):  
    
    sessao = request.session['user']
    viagens = Viagem.objects.filter(usuario=sessao)
    return render(request,"viagens.html",{'viagens':viagens})  



def editar(request, id):  
    viagem = Viagem.objects.get(id=id)  
    return render(request,'editar_viagem.html', {'viagem':viagem})  

def update(request, id):  
    viagem = Viagem.objects.get(id=id)  
    form = ViagemForm(request.POST, instance = viagem)  
    if form.is_valid():  
        viagem=form.save(commit=False)
        viagem.duracao = form.cleaned_data.get("duracao") 
        viagem.lugar= form.cleaned_data.get("lugar")  
        viagem.updated_at = datetime.now()
        v_id = form.cleaned_data.get('v_id')
        viagem.save()   
        messages.success(request, "Viagem atualizada com sucesso")  
        return redirect("/viagens")  
    return render(request, 'editar_viagem.html', {'viagem': viagem})  


def excluir(request, id):  
    viagem = Viagem.objects.get(id=id)  
    viagem.delete()
    messages.success(request, "Viagem excluida com sucesso")
    return redirect("/viagens")  


