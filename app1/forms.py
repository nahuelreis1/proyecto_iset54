from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AlumnoPrueba, CustomUser

class AlumnoPruebaForm (forms.ModelForm):
    class Meta:
        model = AlumnoPrueba
        fields = '__all__'
        
        
class CustomerUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address')
    