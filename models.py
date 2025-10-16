from django.db import models

# Create your models here.

class Producto(models.Model):
    # id será el campo automático de Django (pk)
    nombre = models.CharField(max_length=150, unique=True)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    existencias = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']