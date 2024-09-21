from django.shortcuts import render, redirect
from .forms import AlumnoPruebaForm

# Create your views here.

def home(request):
    form = AlumnoPruebaForm()
    context = {'form':form}
    return render(request, 'home.html', context)

def prueba(request):
    return render(request, 'prueba.html')


