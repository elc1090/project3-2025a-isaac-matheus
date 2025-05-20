from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home_view(request):
    lutadores = Lutador.objects.all()  # busca todos os lutadores do banco
    contexto = {'lutadores': lutadores}
    return render(request, 'template_home.html', contexto)


def exemplo_view(request):
    return HttpResponse("Essa é a view de exemplo") # retorna uma resposta em html