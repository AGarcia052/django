from django.core.management.base import BaseCommand
from pruebadb.models import Personas, Vuelo, UsuariosVuelos, Ciudades, Direccion, Aviones


class Command(BaseCommand):
    help = 'Carga datos iniciales'

    def handle(self, *args, **kwargs):

        if not  Direccion.objects.exists():
            for i in range(1, 100):
                direccion = Direccion(cp=f"cp{i}", calle=f"calle{i}")
                direccion.save()
        else:
            self.stdout.write(self.style.WARNING('La tabla direcciones ya está cargada'))
            self.stdout.write(self.style.ERROR('ERROR'))
            self.stdout.write(self.style.SUCCESS('EXITO'))