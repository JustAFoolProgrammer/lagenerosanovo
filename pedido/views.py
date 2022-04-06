from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Pedido
from .forms import PedidoForm

APP_LABEL = 'Pedido'

class PedidoListView(ListView):
    model = Pedido
    list_fields = all
    app_label = APP_LABEL

class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'pedido/pedido_form.html'
    app_label = APP_LABEL
    fields = '__all__'
