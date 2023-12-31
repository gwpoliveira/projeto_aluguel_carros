# Generated by Django 5.0 on 2023-12-18 12:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_carros', '0004_remove_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contratoaluguel',
            name='devolvido',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefoneCliente',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefoneFuncionario',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Contato:'),
        ),
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_devolucao', models.DateTimeField(default=django.utils.timezone.now)),
                ('danos_observados', models.TextField(blank=True)),
                ('contrato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='devolucao', to='aluguel_carros.contratoaluguel')),
            ],
        ),
    ]
