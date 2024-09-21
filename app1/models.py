from django.db import models

# Create your models here.


class AlumnoPrueba(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    carrer = models.CharField(max_length=200)