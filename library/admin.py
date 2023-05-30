from django.contrib import admin
from library.models import Lector, Autor, Genero, Editorial, Idioma, Libro, Prestamo

# Register your models here.
admin.site.register(Lector)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Libro)
admin.site.register(Prestamo)
