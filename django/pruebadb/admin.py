from django.contrib import admin
from .models import Personas,Vuelo,UsuariosVuelos,Ciudades,Direccion,Aviones

# Register your models here.
admin.site.register(Personas)
admin.site.register(Vuelo)
admin.site.register(UsuariosVuelos)
admin.site.register(Ciudades)
admin.site.register(Direccion)
admin.site.register(Aviones)
