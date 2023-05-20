from django.shortcuts import render
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
from django.db.models.functions import Coalesce

def home(request):  
    if 'user' not in request.session:
          sessao = request.user.email
    else:
        sessao = request.session['user']

    

    viagens = Viagem.objects.filter(usuario=sessao)

    filtro_viagem = Viagem.objects.only('id').filter(usuario=sessao)
    filtro_galeria = Galeria.objects.only('id').filter(v_id__in=filtro_viagem)


    forum = Forum.objects.filter(autor=sessao)
    comentario = Comentario.objects.filter(autor=sessao)


    atividades = Atividade.objects.filter(v_id__in=filtro_viagem)

    galeria = Galeria.objects.filter(v_id__in=filtro_viagem)

    fotogaleria =  FotoGaleria.objects.filter(v_gal__in=filtro_galeria)

    roteiros = Roteiro.objects.filter(v_id__in=filtro_viagem)
            
    custo = Custo.objects.filter(v_id__in=filtro_viagem)
            
    custo_total = custo.aggregate(sum=Sum('valor'))
            

    context  = {
                'object_list': custo,
                'custo_total': custo_total,
                'viagens':viagens,
                'forum':forum,
                'comentario':comentario,
                'atividades':atividades,
                'galeria':galeria,
                'fotogaleria':fotogaleria,
                'roteiros':roteiros,
            }
    return render(request,"home.html",context)  


