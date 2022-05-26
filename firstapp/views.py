from django.shortcuts import redirect, render

from .models import Cadastro_Clientes


def pagina_inicial(request):
    cadastro = Cadastro_Clientes.objects.all()
    dados = {'cadastros': cadastro}
    return render(request, 'firstapp/html/model-page.html', dados)


def pagina_teste(request):
    cadastro = Cadastro_Clientes.objects.all()
    dados = {'cadastros': cadastro}
    return render(request, 'firstapp/html/teste.html', dados)


def submit_post(request):
    if request.POST:
        nome = request.POST.get('nome_cliente')
        email = request.POST.get('email_cliente')
        celular = request.POST.get('celular_cliente')
        cidade = request.POST.get('cidade_cliente')
        Cadastro_Clientes.objects.create(
            nome=nome, email=email, numero_celular=celular, cidade=cidade)
    return redirect('/')
