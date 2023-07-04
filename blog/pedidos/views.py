from django.shortcuts import render
from django.views.generic import TemplateView
from pedidos.models import Pedido

# Create your views here.
class PedidoView(TemplateView):
  template_name = 'pedidos.html'
  
  def get(self, request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    print(pedidos)
    return render(request, self.template_name, { 'pedidos': pedidos })