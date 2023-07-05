from django.db import models

# Create your models here.
class Estado(models.Model):
  nombre = models.CharField(max_length=20, null=False, blank=False)

  def __str__(self):
    return self.nombre

class FormaPago(models.Model):
  nombre = models.CharField(max_length=20, null=False, blank=False)

  def __str__(self):
    return self.nombre

class Pedido(models.Model):
  numero = models.CharField(max_length=10, null=False, blank=False, db_index=True, default='0000000000')
  fecha = models.DateField(auto_now_add=True)
  total = models.DecimalField(max_digits=10, decimal_places=2)
  usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False)
  estado = models.ForeignKey('Estado', on_delete=models.CASCADE, null=False)
  forma_pago = models.ForeignKey('FormaPago', on_delete=models.CASCADE, null=False)
  deleted = models.BooleanField(default=False)

  def __str__(self):
    return str(self.id)

class Productos(models.Model):
  nombre = models.CharField(max_length=100, null=False, blank=False)
  precio = models.DecimalField(max_digits=10, decimal_places=0)

  def __str__(self):
    return self.nombre

class PedidoDetalle(models.Model):
  pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, null=False)
  producto = models.ForeignKey('Productos', on_delete=models.CASCADE, null=False)
  cantidad = models.IntegerField(null=False)
  precio = models.DecimalField(max_digits=10, decimal_places=0)
  total = models.DecimalField(max_digits=10, decimal_places=0)

  def __str__(self):
    return str(self.id)