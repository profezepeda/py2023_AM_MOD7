from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from pedidos.models import Pedido, Productos, PedidoDetalle
from pedidos.forms import FormularioPedido, FormularioDetallePedido

# Create your views here.
class PedidoView(TemplateView):
  template_name = 'pedidos.html'

  def get(self, request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, self.template_name, { 'pedidos': pedidos })

class PedidoEliminarView(DeleteView):
  model = Pedido
  template_name = 'pedido_eliminar.html'
  success_url = reverse_lazy('pedidos')

class PedidoCrearView(TemplateView):
  template_name = 'pedido_agregar.html'

  def get(self, request):
    formulario = FormularioPedido()
    return render(request, self.template_name, { 'form': formulario })

  def post(self, request):
    formulario = FormularioPedido(request.POST)
    if formulario.is_valid():
      pedido = Pedido()
      pedido.numero = formulario.cleaned_data['numero']
      pedido.fecha = formulario.cleaned_data['fecha']
      pedido.estado_id = formulario.cleaned_data['estado']
      pedido.forma_pago_id = formulario.cleaned_data['forma_pago']
      pedido.total = 0
      pedido.usuario_id = 1
      pedido.save()
      return redirect('/pedidos/' + str(pedido.id))
      # return render(request, 'pedido_crear.html', { 'form': formulario })
    else:
      return render(request, 'pedido_editar.html', { 'form': formulario })

class PedidoEditarView(TemplateView):
  template_name = 'pedido_editar.html'

  def get(self, request, pk):
    form_detalle = FormularioDetallePedido()
    productos = Productos.objects.all().order_by('nombre')
    lista_productos = [(producto.id, producto.nombre) for producto in productos]
    form_detalle.fields['producto'].choices = lista_productos
    form_detalle.fields['id'].initial = pk
    try:
      pedido = Pedido.objects.get(id=pk)
      formulario = FormularioPedido(initial = pedido.__dict__)
    except:
      return render(request, '404.html')
    return render(request, self.template_name, { 'form': formulario, 'pedido': pedido, 'form_detalle': form_detalle })

  def post(self, request, pk):
    formulario = FormularioPedido(request.POST)
    if formulario.is_valid():
      pedido = Pedido.objects.get(id=formulario.cleaned_data['id'])
      pedido.numero = formulario.cleaned_data['numero']
      pedido.fecha = formulario.cleaned_data['fecha']
      pedido.estado_id = formulario.cleaned_data['estado']
      pedido.forma_pago_id = formulario.cleaned_data['forma_pago']
      pedido.save()
    return render(request, 'pedido_editar.html', { 'form': formulario })

class PedidoDetalleView(TemplateView):

  def post(self, request):
    formulario = FormularioDetallePedido(request.POST)
    productos = Productos.objects.all().order_by('nombre')
    lista_productos = [(str(producto.id), producto.nombre) for producto in productos]
    formulario.fields['producto'].choices = lista_productos
    if formulario.is_valid():
      pedido = Pedido.objects.get(id=formulario.cleaned_data['id'])
      producto = Productos.objects.get(id=formulario.cleaned_data['producto'])
      cantidad = formulario.cleaned_data['cantidad']
      precio = formulario.cleaned_data['precio']
      total = cantidad * precio
      pedido.total += total
      pedido.save()
      pedido_detalle = PedidoDetalle()
      pedido_detalle.pedido = pedido
      pedido_detalle.producto = producto
      pedido_detalle.cantidad = cantidad
      pedido_detalle.precio = precio
      pedido_detalle.total = total
      pedido_detalle.save()
      return redirect('/pedidos/' + str(pedido.id))
    print(formulario.errors)
    return redirect('/pedidos')