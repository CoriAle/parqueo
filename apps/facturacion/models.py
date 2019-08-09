from django.db import models
from apps.vehiculo.models import Vehiculo

# Create your models here.


class Cliente(models.Model):
	nit = models.CharField(max_length=10, default='cf')
	nombre = models.CharField(max_length=300)
	apellido = models.CharField(max_length=300)
	direccion = models.TextField(default='Ciudad')
	estado= models.BooleanField(default=False)

	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"

	def __str__(self):
		return nit

class Encabezado(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
	estado = models.BooleanField(default=True)
	total = models.FloatField()
	numero = models.CharField(max_length=50, null=True, blank=True)
	detalle = models.ManyToManyField(Vehiculo, through='facturacion.Detalle')

	class Meta:
		verbose_name = "Encabezado"
		verbose_name_plural = "Encabezados"

	def __str__(self):
		return numero


class Detalle(models.Model):
	ingreso=models.DateTimeField(auto_now_add=True)
	salida = models.DateTimeField(null=True, blank=True)
	subtotal = models.FloatField()
	factura = models.ForeignKey(Encabezado,'detalle', related_name='detalle_factura')
	vehiculo = models.ForeignKey(Vehiculo, related_name='detalle',  on_delete=models.CASCADE)


	class Meta:
		verbose_name = "Detalle"
		verbose_name_plural = "Detalles"

	def __str__(self):
		return self.subtotal
	
	

