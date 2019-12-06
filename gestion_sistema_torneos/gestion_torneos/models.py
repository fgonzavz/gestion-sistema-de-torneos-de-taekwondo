from django.db import models

# Create your models here.


class MaestroModel(models.Model):
    run=models.TextField(unique=True)
    nombres=models.TextField()
    apellidos=models.TextField()
    telefono=models.TextField()
    grado=models.TextField()
    #direccion=models.TextField()
    email=models.TextField()
    class Meta:
        db_table='maestro'



