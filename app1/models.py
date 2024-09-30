from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.


class AlumnoPrueba(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    carrer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class CustomUser(AbstractUser):
    # Campos personalizados
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    # Cambiamos las relaciones inversas con related_name
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username