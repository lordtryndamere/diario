from django.db import models

# Create your models here.
class Deporte(models.Model):
	id = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return '{}'.format(self.nombre)

class Jugador(models.Model):
	id = models.IntegerField(primary_key=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	fecha_nacimiento = models.DateField()
	email = models.EmailField(max_length=200)
	deporte = models.ForeignKey(Deporte, null=True, blank=True, on_delete=models.CASCADE)
	