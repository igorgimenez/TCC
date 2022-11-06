from django.shortcuts import render,redirect
from atividades.forms import AtividadesForm  
from atividades.models import  Atividade
from viagem.models import Viagem 
from datetime import datetime
from django.contrib import messages


def atividades(request,id):  
    atividades = Atividade.objects.filter(v_id = id)
    v_id = id
    return render(request,"atividades.html",{'atividades':atividades, 'v_id': v_id })  
    
    

def nova_atividade(request,id):  

    context ={}
  
   
    initial_dict = {
        "v_id" : id,
    }
  
    
    form = AtividadesForm(request.POST or None, initial = initial_dict)
  
    context['form']= form
    return render(request, "nova_atividade.html", context)
   



def criar(request):



    context = {}
    if request.method == "POST": 
        form = AtividadesForm(request.POST, request.FILES) 
        if form.is_valid(): 
            v_id = form.cleaned_data.get("v_id") 
            duracao = form.cleaned_data.get("duracao") 
            lugar= form.cleaned_data.get("lugar") 
            obs= form.cleaned_data.get("obs") 
            img= form.cleaned_data.get("img") 
            

            obj = Atividade.objects.create( 
                                 v_id = v_id, 
                                 duracao=duracao,
                                 lugar=lugar,
                                 obs=obs, 
                                 img = img
                                  
                                 ) 
            obj.save() 
            print(obj)
            url_id= str(v_id)
            messages.success(request, "Atividade criada com sucesso")
            return redirect ('/atividades/%s'%url_id) 
    else: 
        form = AtividadesForm()
        context['form'] = form
        return render( request, "nova_atividade.html", context) 



def editar(request, id):  
    atividade = Atividade.objects.get(id=id)  
    return render(request,'editar_atividade.html', {'atividade':atividade})  

    

def update(request, id):  
    atividade = Atividade.objects.get(id=id)  
    form = AtividadesForm(request.POST, request.FILES, instance = atividade)  
    if form.is_valid(): 
        atividade=form.save(commit=False)
        atividade.duracao = form.cleaned_data.get("duracao") 
        atividade.lugar= form.cleaned_data.get("lugar") 
        atividade.obs= form.cleaned_data.get("obs") 
        atividade.img= form.cleaned_data.get("img") 
        atividade.updated_at = datetime.now()
        v_id = form.cleaned_data.get('v_id')
        atividade.save() 
        url_id= str(v_id) 
        messages.success(request, "Atividade atualizada com sucesso")
        return redirect ('/atividades/%s'%url_id)    
    return render(request, 'editar_atividade.html', {'atividade': atividade})
	
	
	

def excluir(request, id):  
    atividade = Atividade.objects.get(id=id)  
    atividade.delete()  
    campo = 'v_id'
    valor = getattr(atividade, campo)
    messages.success(request, "Atividade excluida com sucesso")
    url_id= str(valor)
    return redirect ('/atividades/%s'%url_id)