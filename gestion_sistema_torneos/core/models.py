from django.db import models

class Maestro(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    grado = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE) 
    imagen = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.nombre


class Competidores(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    grado = models.CharField(max_length=30)
    rut = models.CharField(max_length=11)
    equipo= models.ForeignKey(Equipo,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Torneo(models.Model):
    fecha= models.DateField()
    nombre=models.CharField(max_length=25)
    equipo_participante=models.ForeignKey(Equipo,on_delete=models.CASCADE)
    competidores_participantes=models.ForeignKey(Competidores,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre




