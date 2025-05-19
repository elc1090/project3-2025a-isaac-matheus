from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    # dicionário com dados para passar ao template de exemplo
    contexto = {
        'titulo': 'Lutador boboca',
        'usuario': {
            'nome': 'Homem torta',
            'idade': 666,
            'email': 'homemtorta@gmail.com'
        },
        'ataques': ['Tortura', 'Entorta', 'Torta'],
        'existe': True
    }
    return render(request, 'template_home.html', contexto) # retorna um html com um dicionário


def exemplo_view(request):
    return HttpResponse("Essa é a view de exemplo") # retorna uma resposta em html