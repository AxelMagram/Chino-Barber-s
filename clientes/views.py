from django.shortcuts import render


def inicio(request):
    return render(request, 'clientes/inicio.html')


def sobre_nosotros(request):
    return render(request, 'clientes/sobre_nosotros.html')
