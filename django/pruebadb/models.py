from django.db import models

# Create your models here.

class Direccion(models.Model):
    cp = models.CharField(max_length=20)
    calle = models.CharField(max_length=30)
    def __str__(self):
        return self.cp+" "+self.calle

class Ciudades(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Aviones(models.Model):
    nombreAvion = models.CharField(max_length=30)
    def __str__(self):
        return self.nombreAvion
class Personas(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    edad = models.IntegerField()
    dni = models.CharField(blank=True, null=True,max_length=9)
    activo = models.CharField(max_length=2, default="s")
    adolfo = models.CharField(max_length=24, blank=True, null=True)
    idDireccion = models.ForeignKey(Direccion,blank=True,null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre+" "+self.apellidos

class Vuelo(models.Model):
    idCiudadOrigen = models.ForeignKey(Ciudades, on_delete=models.CASCADE,related_name="fkciudadOrigen")
    idCiudadDestino = models.ForeignKey(Ciudades, on_delete=models.CASCADE, related_name="fkciudadDestino")
    fechaVuelo = models.DateField()
    estadoVuelo = models.CharField(max_length=20)
    idAvion = models.ForeignKey(Aviones, on_delete=models.CASCADE)
    def __str__(self):
        return self.fechaVuelo

class UsuariosVuelos(models.Model):
    idPasajero = models.ForeignKey(Personas, on_delete=models.CASCADE)
    idVuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE)
    precioBillete = models.IntegerField()


