from django.contrib import admin
from principal.models import Publicacion

class PublicacionAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'fecha_creacion', 'fecha_publicacion', 'autor']
  list_filter = ['fecha_creacion', 'fecha_publicacion', 'autor']
  search_fields = ['titulo', 'contenido']
  ordering = ['fecha_creacion', 'fecha_publicacion']
  fields = ['titulo', 'resumen', 'slug', 'contenido', 'fecha_creacion', 'fecha_publicacion', 'autor']
  readonly_fields = ['fecha_creacion', 'fecha_publicacion']



admin.site.register(Publicacion, PublicacionAdmin)
# Register your models here.
