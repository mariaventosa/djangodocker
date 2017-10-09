from django.db import models

# Create your models here.

class Contacto(models.Model):
	nombre = models.CharField(max_length = 20)
	apellido = models.CharField(max_length = 20)


class Telefono(models.Model):
	telefono = models.CharField(max_length = 10)
	opciones_telefono = ("Casa", "Celular", "Trabajo")
	tipo = models.CharField(max_length = 10, choices = opciones_telefono, default = "Celular")