# Generated by Django 5.0 on 2023-12-18 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel_carros', '0005_contratoaluguel_devolvido_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Devolucao',
        ),
    ]