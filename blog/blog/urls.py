"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal.views import Muestra
from django.views.generic import TemplateView
from pedidos.views import PedidoView, PedidoEliminarView, PedidoEditarView, PedidoCrearView, PedidoDetalleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publicacion/<str:idpublicacion>', Muestra.as_view(), name='muestra'),
    path('pedidos/', PedidoView.as_view(), name='pedidos'),
    path('pedidos/<int:pk>/delete/', PedidoEliminarView.as_view(), name='pedido_eliminar'),
    path('pedidos/create/', PedidoCrearView.as_view(), name='pedido_agregar'),
    path('pedidos/<int:pk>', PedidoEditarView.as_view(), name='pedido_editar'),
    path('pedidos/detalle/', PedidoDetalleView.as_view(), name='agregar_detalle')
]
