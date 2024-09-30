from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import AlumnoPruebaForm, CustomerUserForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AlumnoPruebaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlumnoPruebaForm()

    # Obtiene el nombre de usuario de la sesión, si existe
    username = request.session.get('username')

    # Eliminar el nombre de usuario de la sesión después de usarlo (opcional)
    # del request.session['username']

    return render(request, 'home.html', {
        'form': form,
        'username': username,  # Pasa el nombre de usuario al contexto
    })


def prueba(request):
    return render(request, 'prueba.html')


def registerUser(request):
    if request.method == 'POST':
        form2 = CustomerUserForm(request.POST)
        if form2.is_valid():
            user = form2.save()
            login(request, user)
            # Almacena el nombre de usuario en la sesión
            request.session['username'] = user.username  
            return redirect('home')
        else:
            print(form2.errors)
    else:
        form2 = CustomerUserForm()
        
    return render(request, 'register.html', {'form2': form2})


