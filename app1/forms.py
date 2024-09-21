from django import forms

from .models import AlumnoPrueba

class AlumnoPruebaForm (forms.ModelForm):
    class Meta:
        model = AlumnoPrueba
        fields = '__all__'