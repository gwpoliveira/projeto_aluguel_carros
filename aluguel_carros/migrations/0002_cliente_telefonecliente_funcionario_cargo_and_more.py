# Generated by Django 5.0 on 2023-12-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='telefoneCliente',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.CharField(default='Vendedor', max_length=100, verbose_name='Cargo:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='telefoneFuncionario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
