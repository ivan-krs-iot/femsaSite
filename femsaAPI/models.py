from django.db import models

# Create your models here.
class vehiculo(models.Model):
	epc = models.CharField(max_length=50)
	placa = models.CharField(max_length=10)
	

class conductor(models.Model):
	epc = models.CharField(max_length=50)
	nombre = models.CharField(max_length=10)
	

class caja(models.Model):
	epc = models.CharField(max_length=50)
	id_caja = models.CharField(max_length=50)



class registro(models.Model):
	placa = models.CharField(max_length=10)
	nombre = models.CharField(max_length=10)
	id_caja = models.CharField(max_length=50)
	movimiento = models.CharField(max_length=10)
	estado = models.CharField(max_length=10)
	fecha = models.DateTimeField(auto_now_add=True)
	
