from django.shortcuts import render

# Create your views here.

def Index(request):

    return render (request, 'inicio.html')

def Pagina(request):

    return render (request, 'pagina.html')