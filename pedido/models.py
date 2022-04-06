from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pedido(models.Model):
    des_pedido = models.CharField('Descricao do pedido', max_length=255)
    nome = models.CharField('Nome', primary_key=True, max_length=255)
    imagem = models.ImageField('Imagem', upload_to='media')
    diahora = models.DateTimeField(auto_now_add=True)
    diahora_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-diahora',)
        verbose_name = 'Criar Pedido'
        app_label='Pedido'