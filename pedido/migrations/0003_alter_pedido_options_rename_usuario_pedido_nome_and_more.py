# Generated by Django 4.0.3 on 2022-03-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_remove_pedido_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ('-diahora',), 'verbose_name': 'Criar Pedido'},
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='usuario',
            new_name='nome',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='des_pedido',
            field=models.CharField(max_length=255, verbose_name='Descricao do pedido'),
        ),
    ]
