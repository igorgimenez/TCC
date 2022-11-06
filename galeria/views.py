from telnetlib import GA
from django.shortcuts import render,redirect
from django.views import  View
import galeria
from galeria.forms import GaleriaForm,FotoGaleriaForm  
from galeria.models import  Galeria, FotoGaleria
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from viagem.models import  Viagem
from datetime import datetime
from django.contrib import messages


def galerias(request,id):  
    galeria = Galeria.objects.filter(v_id = id)
    v_id = id
    return render(request,"galeria.html",{'galeria':galeria, 'v_id': v_id })  



def nova_galeria(request,id):  
   
    context ={}
 
    initial_dict = {
        "v_id" : id,
    }
  
    form = GaleriaForm(request.POST or None, initial = initial_dict)
  
    context['form']= form
    return render(request, "nova_galeria.html", context)
    
   



def criargaleria(request):

    context = {}
    if request.method == "POST": 
        form = GaleriaForm(request.POST) 
        if form.is_valid(): 
            v_id = form.cleaned_data.get("v_id") 
            nome = form.cleaned_data.get("nome") 
            obj = Galeria.objects.create( 
                                 v_id = v_id, 
                                 nome=nome
                                 ) 
            obj.save() 
            print(obj)
            url_id= str(v_id)
            messages.success(request, "Galeria criada com sucesso")
            return redirect ('/galerias/%s'%url_id) 
            
                                
    else: 
        form = GaleriaForm()
        context['form'] = form
        return render( request, "nova_galeria.html", context) 



def fotos_galeria(request,id):  
    fotos = FotoGaleria.objects.filter(v_gal= id)
    v_gal = id
    return render(request,"foto_galeria.html",{'fotos':fotos, 'v_gal': v_gal })



def adicionar_fotosgaleria(request,id):  
    v_gal=id
    return render(request, "adicionar_fotosgaleria.html", {'v_gal': v_gal} )



def criar_fotogaleria(request):
    
    if request.method == "POST":
        v_gal=request.POST.get('v_gal')
        images = request.FILES.getlist('images')
        for image in images:
             FotoGaleria.objects.create(img=image,v_gal=v_gal)
        images = FotoGaleria.objects.all()
        url_id= str(v_gal)
        messages.success(request, "Fotos adicionadas com sucesso")
        return redirect ('/fotos_galeria/%s'%url_id)
    return render(request, 'adicionar_fotosgaleria.html', {'images': images})


def editar(request, id):  
    galeria = Galeria.objects.get(id=id)  
    return render(request,'editar_galeria.html', {'galeria':galeria})  


def update(request, id):  
    galeria = Galeria.objects.get(id=id)  
    form = GaleriaForm(request.POST, instance = galeria)  
    if form.is_valid(): 
        galeria=form.save(commit=False)
        galeria.nome = form.cleaned_data.get("nome") 
        galeria.updated_at = datetime.now()
        v_id = form.cleaned_data.get('v_id')
        galeria.save() 
        url_id= str(v_id) 
        messages.success(request, "Galeria atualizada com sucesso")
        return redirect ('/galerias/%s'%url_id)    
    return render(request, 'editar_galeria.html', {'galeria': galeria})

def excluir(request, id):  
    galeria = Galeria.objects.get(id=id)  
    galeria.delete()  
    campo = 'v_id'
    valor = getattr(galeria, campo)
    messages.success(request, "Galeria excluida com sucesso")
    url_id= str(valor)
    return redirect ('/galerias/%s'%url_id)