from django.shortcuts import get_object_or_404, redirect, render

from .forms import UpdateForm
from .models import Cadastro_Clientes


def pagina_inicial(request):
    cadastro = Cadastro_Clientes.objects.all().order_by('-id')
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


def edit_post(request, pk):
    atualizar = get_object_or_404(Cadastro_Clientes, pk=pk)
    form = UpdateForm(instance=atualizar)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=atualizar)
        if form.is_valid():
            atualizar.save()
            return redirect('/')
        else:
            return render(request, 'firstapp/html/editar-cadastro.html', {'form': form, 'atualizar': atualizar})  # noqa
    else:
        return render(request, 'firstapp/html/editar-cadastro.html', {'form': form, 'atualizar': atualizar})  # noqa


def delete_cadastro(request, id_cadastro):
    Cadastro_Clientes.objects.filter(id=id_cadastro).delete()
    return redirect('/')
