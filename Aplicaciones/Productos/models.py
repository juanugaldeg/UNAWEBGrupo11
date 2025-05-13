from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    lote = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField()
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.PositiveIntegerField()
    unidad_medida = models.CharField(max_length=20)  # Ej: "comprimidos", "ml", "frascos"
    requiere_receta = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.codigo, self.descripcion)