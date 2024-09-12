from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def prueba(request):
    return render(request, 'prueba.html')
