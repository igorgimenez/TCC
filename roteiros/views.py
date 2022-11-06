from ctypes import HRESULT
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from roteiros.forms import RoteiroForm, RoteiroEditForm
from roteiros.models import  Roteiro
from viagem.models import  Viagem
from roteiros.forms import RoteiroFormset, RoteiroModelFormset
from roteiros.filters import RoteiroFilter


from django.template.loader import render_to_string
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse

from django.contrib import messages
from datetime import datetime




def roteiros(request,id):  
    roteiro_list = Roteiro.objects.filter(v_id=id).order_by('dia','horario_inicial')
    roteiro_filter = RoteiroFilter(request.GET, queryset=roteiro_list)
    v_id = id
    return render(request, 'roteiros.html', {'filter': roteiro_filter,'v_id': v_id})


def criar_roteiros(request,id):

        viagens = Viagem.objects.filter(id=id)
     


        template_name = 'store/criar_roteiro.html'
        

        if request.method == 'GET':
            formset = RoteiroFormset(request.GET or None)
        elif request.method == 'POST':
            formset = RoteiroFormset(request.POST)
            if formset.is_valid():
                for form in formset:
                    horario_inicial = form.cleaned_data.get('horario_inicial')
                    horario_final = form.cleaned_data.get('horario_final')
                    lugar = form.cleaned_data.get('lugar')
                    acao = form.cleaned_data.get('acao')
                    v_id =  form.cleaned_data.get('v_id')
                    dia =  form.cleaned_data.get('dia')
                    if horario_inicial:
                    
                        Roteiro(horario_inicial=horario_inicial,horario_final=horario_final,lugar=lugar,acao=acao,v_id=id, dia=dia).save()
                        
                        url_id= str(id)
                messages.success(request, "Roteiro criado com sucesso")      
                return redirect('/roteiros/%s'%url_id)

        return render(request, template_name, {
            'formset': formset,
            'viagens':viagens,
        })


def editar(request, id):  
    roteiro = Roteiro.objects.get(id=id)  
    return render(request,'editar_roteiro.html', {'roteiro':roteiro})  

def update_roteiro(request, id):  
    roteiro = Roteiro.objects.get(id=id)  
    form = RoteiroEditForm(request.POST, instance = roteiro)
    if form.is_valid():  
        roteiro=form.save(commit=False)
        roteiro.horario_inicial = form.cleaned_data.get("horario_inicial") 
        roteiro.horario_final= form.cleaned_data.get("horario_final") 
        roteiro.lugar= form.cleaned_data.get("lugar") 
        roteiro.acao= form.cleaned_data.get("acao") 
        roteiro.updated_at = datetime.now()
        v_id = form.cleaned_data.get('v_id')
        roteiro.save() 
        url_id= str(v_id)
        messages.success(request, "Roteiro atualizado com sucesso")  
        return redirect ('/roteiros/%s'%url_id)   
    return render(request, 'editar_roteiro.html', {'roteiro': roteiro})  


def excluir(request, id):  
    roteiro = Roteiro.objects.get(id=id)
    roteiro.delete()
    campo = 'v_id'
    valor = getattr(roteiro, campo)
    messages.success(request, "Roteiro excluido com sucesso")
    url_id= str(valor)
    return redirect ('/roteiros/%s'%url_id)
     


    

def render_pdf_filtro(request,id,dia):
    path = "roteiro_pdftemplate.html"
    
    roteiro_list = Roteiro.objects.filter(v_id=id, dia=dia).order_by('dia','horario_inicial')
    roteiro_filter = RoteiroFilter(request.GET, queryset=roteiro_list)
    v_id = id
    
    
    html = render_to_string('roteiro_pdftemplate.html',{'filter': roteiro_filter,'v_id': v_id,'dia': dia})
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)





def render_pdf(request,id):
    path = "roteiro_pdftemplate.html"
   
    roteiro_list = Roteiro.objects.filter(v_id=id).order_by('dia','horario_inicial')
    roteiro_filter = RoteiroFilter(request.GET, queryset=roteiro_list)
    v_id = id
    
    
    html = render_to_string('roteiro_pdftemplate.html',{'filter': roteiro_filter,'v_id': v_id})
    io_bytes = BytesIO()
    
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), io_bytes)
    
    if not pdf.err:
        return HttpResponse(io_bytes.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error while rendering PDF", status=400)



