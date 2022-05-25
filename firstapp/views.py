from django.shortcuts import render

from .models import Cadastro_Clientes


def pagina_inicial(request):
    cadastro = Cadastro_Clientes.objects.all()
    dados = {'cadastros': cadastro}
    return render(request, 'firstapp/html/model-page.html', dados)


def pagina_teste(request):
    cadastro = Cadastro_Clientes.objects.all()
    dados = {'cadastros': cadastro}
    return render(request, 'firstapp/html/teste.html', dados)
