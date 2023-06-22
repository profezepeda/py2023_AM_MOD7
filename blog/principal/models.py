import uuid
from django.db.models.query import QuerySet
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Managers
class PublicacionManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(deleted=False)

# Create your models here.
class Publicacion(models.Model):
  idpublicacion = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  titulo = models.CharField(max_length=200, null=False, blank=False)
  resumen = models.CharField(max_length=255, null=False, blank=False)
  slug = models.SlugField(max_length=255, null=False, blank=False, unique=True)
  contenido = models.TextField(null=False, blank=False)
  fecha_creacion = models.DateTimeField(default=timezone.now)
  fecha_publicacion = models.DateTimeField(auto_now_add=True)
  autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
  deleted = models.BooleanField(default=False)
  # visitas = models.ManyToManyField(User, related_name='visitas', blank=True)
  visitas = models.ManyToManyField(User, through='Visita', related_name='visitas', blank=True)

  objects = PublicacionManager()

  def delete(self, *args, **kwargs):
    self.deleted = True
    self.save()

  def publicar(self):
    self.fecha_creacion = timezone.now()
    self.save()

  def __str__(self):
      return self.titulo

class Comentario(models.Model):
  fechahora = models.DateTimeField(default=timezone.now)
  comentario = models.TextField(null=False, blank=False)
  publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=False)
  usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

class Perfil(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  telefono = models.CharField(max_length=20, null=True, blank=True)
  direccion_calle = models.CharField(max_length=255, null=True, blank=True)
  direccion_numero = models.CharField(max_length=10, null=True, blank=True)
  direccion_depto = models.CharField(max_length=5, null=True, blank=True)

class Visita(models.Model):
  publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, null=False)
  usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
  fechahora = models.DateTimeField(default=timezone.now)