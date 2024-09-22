from django.shortcuts import render, redirect
from .forms import AlumnoPruebaForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AlumnoPruebaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlumnoPruebaForm()
    return render(request, 'home.html', {'form':form})

def prueba(request):
    return render(request, 'prueba.html')


