from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('prueba/', views.prueba, name='prueba'),
    path('register/', views.registerUser, name='register'),
]