from django.forms import forms
from .models import Pedido

class PedidoForm(forms.Form):
    class Meta:
        model = Pedido
        fields = '__all__'