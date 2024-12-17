from django.apps import AppConfig

class PruebadbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pruebadb'

    def ready(self):
        from .models import Personas, Vuelo, UsuariosVuelos, Ciudades, Direccion, Aviones
        direccion = Direccion(cp="cp3",calle="calle4")
        direccion.save()

cp1
cp2
cp3

