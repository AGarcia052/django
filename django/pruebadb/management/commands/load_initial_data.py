from django.core.management.base import BaseCommand
from pruebadb.models import Personas, Vuelo, UsuariosVuelos, Ciudades, Direccion, Aviones

class Command(BaseCommand):
    help = 'Carga datos iniciales'

    def handle(self, *args, **kwargs):
        try:
            direccion = Direccion.objects.get(pk=40)
            direccion.calle ="23"
            direccion.save()

            persona = Personas(nombre="Carlos",apellidos="ddd", idDireccion=direccion)
            persona.save()
        except Direccion.DoesNotExist:
            self.stdout.write(self.style.ERROR('No existe '))
        except Exception as e:
            print(f"Ocurrió un error: {e}")
            self.stdout.write(self.style.WARNING('Otro error'))


