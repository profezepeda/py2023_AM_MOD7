from django.shortcuts import render
from django.views.generic import TemplateView
from principal.models import Publicacion, Comentario, Visita
from django.contrib.auth.models import Group, User

# Create your views here.

class Muestra(TemplateView):
  template_name = 'muestra.html'

  def get(self, request, idpublicacion, *args, **kwargs):
    publicacion = Publicacion.objects.get(idpublicacion=idpublicacion)
    if publicacion is None:
      return render(request, '404.html')
    context = {
      "post": publicacion,
      "comentarios": Comentario.objects.filter(publicacion=publicacion).all()
    }
    visita = Visita(publicacion=publicacion)
    visita.save()
    # context["post"] = { "titulo": publicacion.titulo, "contenido": publicacion.contenido}
    return render(request, self.template_name, context)