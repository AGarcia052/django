from django.core.management.base import BaseCommand
from app.models import Personas, Direccion, Ciudades, Aviones, Vuelo, UsuariosVuelos
import random
from datetime import date

class Command(BaseCommand):
    help = 'Cargar datos iniciales para Air Europa'

    def handle(self, *args, **kwargs):
        try:
            if not Ciudades.objects.exists():
                ciudades = []
                for i in range(1, 21):
                    ciudad = Ciudades.objects.create(nombre=f'Ciudad{i}')
                    ciudades.append(ciudad)
                self.stdout.write(self.style.SUCCESS(f'{len(ciudades)} ciudades creadas.'))
            else:
                self.stdout.write(self.style.WARNING('Las ciudades ya existen.'))

            if not Aviones.objects.exists():
                aviones = []
                for i in range(1, 21):
                    avion = Aviones.objects.create(nombreAvion=f'Avion{i}')
                    aviones.append(avion)
                self.stdout.write(self.style.SUCCESS(f'{len(aviones)} aviones creados.'))
            else:
                self.stdout.write(self.style.WARNING('Los aviones ya existen.'))

            if not Personas.objects.exists():
                personas = []
                for i in range(1, 41):
                    direccion = Direccion.objects.create(calle=f'Calle{i}', cp=f'CP{i}')
                    persona = Personas.objects.create(
                        nombre=f'Nombre{i}',
                        apellidos=f'Apellido{i}',
                        edad=random.randint(1, 65),
                        activo="s",
                        idDireccion=direccion
                    )
                    personas.append(persona)
                self.stdout.write(self.style.SUCCESS(f'{len(personas)} personas creadas con sus direcciones.'))
            else:
                self.stdout.write(self.style.WARNING('Las personas ya existen.'))

            if not Vuelo.objects.exists():
                ciudades = Ciudades.objects.all()
                aviones = Aviones.objects.all()
                vuelos = []
                for i in range(1, 16):
                    try:
                        ciudad_origen = random.choice(ciudades)
                        ciudad_destino = random.choice([c for c in ciudades if c != ciudad_origen])
                        avion = random.choice(aviones)

                        vuelo = Vuelo.objects.create(
                            idCiudadOrigen=ciudad_origen,
                            idCiudadDestino=ciudad_destino,
                            fechaVuelo=date.today(),
                            estadoVuelo='destino',
                            idAvion=avion
                        )
                        vuelos.append(vuelo)
                    except Ciudades.DoesNotExist:
                        self.stdout.write(self.style.ERROR('Error: Una de las ciudades no existe.'))
                self.stdout.write(self.style.SUCCESS(f'{len(vuelos)} vuelos creados.'))
            else:
                self.stdout.write(self.style.WARNING('Los vuelos ya existen.'))

            if not UsuariosVuelos.objects.exists():
                personas = Personas.objects.all()
                vuelos = Vuelo.objects.all()
                for vuelo in vuelos:
                    try:
                        pasajero = random.choice(personas)
                        UsuariosVuelos.objects.create(
                            idPasajero=pasajero,
                            idVuelo=vuelo,
                            precioBillete=random.randint(200, 500)
                        )
                    except Personas.DoesNotExist:
                        self.stdout.write(self.style.ERROR('Error: Una de las personas no existe.'))
                    except Vuelo.DoesNotExist:
                        self.stdout.write(self.style.ERROR('Error: El vuelo no existe.'))
                self.stdout.write(self.style.SUCCESS('15 usuarios-vuelos creados.'))
            else:
                self.stdout.write(self.style.WARNING('Los usuarios-vuelos ya existen.'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Ocurrió un error: {e}'))
