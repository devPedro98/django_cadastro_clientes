from django.shortcuts import render


def pagina_inicial(request):
    return render(request, 'firstapp/html/index.html')
