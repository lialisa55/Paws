# Generated by Django 5.0.7 on 2024-07-28 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resgatador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea')], max_length=1)),
                ('microchip', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('especie', models.CharField(max_length=50)),
                ('porte', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')], max_length=1)),
                ('raca', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=100)),
                ('sobre_o_pet', models.TextField()),
                ('adotado', models.BooleanField(default=False)),
                ('data_resgate', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('resgatador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animais', to='vitrine.resgatador')),
            ],
        ),
    ]