from django import forms
from pedidos.models import Estado, FormaPago

class FormularioPedido(forms.Form):
  opciones_estado = Estado.objects.all().values_list('id', 'nombre').order_by('nombre')
  OPCIONES_ESTADO = [(opcion.id, opcion.nombre) for opcion in opciones_estado]
  opciones_forma_pago = FormaPago.objects.all().values_list('id', 'nombre').order_by('nombre')
  OPCIONES_FORMA_PAGO = [(opcion.id, opcion.nombre) for opcion in opciones_forma_pago]

  numero = forms.CharField(label='Número de Pedido', max_length=10, required=True,
                          error_messages={
                            'required': 'El número de pedido es requerido',
                            'max_length': 'El número de pedido no puede superar los 10 caracteres'},
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de Pedido'}),
                          help_text='Ingrese el número de pedido')
  fecha = forms.DateField(label="Fecha", required=True,
                          error_messages={
                            'required': 'La fecha es requerida'},
                          widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha'}),
                          help_text='Ingrese la fecha del pedido')
  estado = forms.ChoiceField(choices=OPCIONES_ESTADO, required=True,
                            error_messages={'required': 'El estado es requerido'},
                            widget=forms.Select(attrs={'class': 'form-control'}),
                            help_text='Seleccione el estado del pedido')
  forma_pago = forms.ChoiceField(choices=OPCIONES_FORMA_PAGO, required=True,
                                error_messages={'required': 'La forma de pago es requerida'},
                                widget=forms.Select(attrs={'class': 'form-control'}),
                                help_text='Seleccione la forma de pago del pedido')