# Generated by Django 3.2.25 on 2024-12-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aviones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAvion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp', models.CharField(max_length=20)),
                ('calle', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVuelo', models.DateField()),
                ('estadoVuelo', models.CharField(max_length=20)),
                ('idAvion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebadb.aviones')),
                ('idCiudadDestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fkciudadDestino', to='pruebadb.ciudades')),
                ('idCiudadOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fkciudadOrigen', to='pruebadb.ciudades')),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosVuelos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioBillete', models.IntegerField()),
                ('idCiudadOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebadb.personas')),
                ('idVuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebadb.vuelo')),
            ],
        ),
    ]