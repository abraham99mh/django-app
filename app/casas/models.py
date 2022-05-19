from django.db import models

# Create your models here.


class House(models.Model):
    nombre = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    dir = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    num_habitacione = models.IntegerField()
    check_in = models.CharField(max_length=10)
    check_out = models.CharField(max_length=10)
    imgs = models.ImageField()
    id_dueño = models.IntegerField()
    precio = models.CharField(max_length=10)
    estatus = models.BooleanField()

    def __str__(self):
        return str(self.nombre)
