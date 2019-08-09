from django.db import models

# Create your models here.
class Marca(models.Model):
	nombre = models.CharField(max_length=100)
	estado = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Marca"
		verbose_name_plural = "Marcas"

	def __str__(self):
		return self.nombre

	def delete(self):
		self.estado = False
		self.save()


class Modelo(models.Model):
	anyo = models.SmallIntegerField()
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='modelo')
	estado = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Modelo"
		verbose_name_plural = "Modelos"

	def __str__(self):
		return str(self.anyo)

class Propietario(models.Model):
	nombre = models.CharField(max_length=300)
	apellido = models.CharField(max_length=300)
	dpi = models.CharField(max_length=15)
	nacimiento = models.DateField(null=True, blank=True)

	class Meta:
		verbose_name = "Propietario"
		verbose_name_plural = "Propietarios"

	def __str__(self):
		return self.nombre + " "+ self.apellido
	

	
class Vehiculo(models.Model):

	placa = models.CharField(max_length=10)
	chasis = models.CharField(max_length=25)
	color = models.CharField(max_length=50)
	modelo = models.ForeignKey(Modelo,  on_delete=models.CASCADE, related_name='vehiculo')
	propietario = models.ForeignKey(Propietario, on_delete= models.CASCADE,related_name='vehiculo')
	class Meta:
		verbose_name = "Vehiculo"
		verbose_name_plural = "Vehiculos"

	def __str__(self):
		pass
		#return self.placa +" "+ self.chasis
	 

