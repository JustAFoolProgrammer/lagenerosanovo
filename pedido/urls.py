from django.urls import path

from . import views

app_name = "pedido"

urlpatterns = [
    path("", views.PedidoListView.as_view(), name="list"),
    path('create/', views.PedidoCreateView.as_view(), name='create'),
]