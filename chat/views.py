from django.shortcuts import render, redirect
from chat.models import Sala, Mensagem
from django.http import HttpResponse, JsonResponse


def chat(request):
    usuario=request.POST.get('usuario_mensagem')
    return render(request, 'chat.html',{'usuario':usuario})

def sala(request, sala):
    if 'user' not in request.session:
        username = request.user.email
        sala_detalhes = Sala.objects.get(nome=sala)
        return render(request, 'sala.html', {
            'username': username,
            'sala': sala,
            'sala_detalhes': sala_detalhes
        })
    else:
        username = request.session['user']
        sala_detalhes = Sala.objects.get(nome=sala)
        return render(request, 'sala.html', {
            'username': username,
            'sala': sala,
            'sala_detalhes': sala_detalhes
        })

def checkview(request):
    if 'user' not in request.session:
         sessao = request.user.email
         sala = request.POST['sala_nome'] + '+' + sessao
         username = sessao
         if Sala.objects.filter(nome=sala).exists():
            return redirect('/'+sala+'/?username='+username)
         else:
            new_sala = Sala.objects.create(nome=sala)
            new_sala.save()
            return redirect('/'+sala+'/?username='+username)
    else:  
        sala = request.POST['sala_nome'] + '+' + request.session['user']
        username = request.session['user']
        if Sala.objects.filter(nome=sala).exists():
            return redirect('/'+sala+'/?username='+username)
        else:
            new_sala = Sala.objects.create(nome=sala)
            new_sala.save()
            return redirect('/'+sala+'/?username='+username)

    



def send(request):
    mensagem = request.POST['mensagem']
    username = request.POST['username']
    sala_id = request.POST['sala_id']

    nova_mensagem = Mensagem.objects.create(value=mensagem, user=username, sala=sala_id)
    nova_mensagem.save()
    return HttpResponse('Mensagem enviada com sucesso')

def BuscaMensagem(request, sala):
    sala_detalhes = Sala.objects.get(nome=sala)

    messages = Mensagem.objects.filter(sala=sala_detalhes.id)
    return JsonResponse({"messages":list(messages.values())})