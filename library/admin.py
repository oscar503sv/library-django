from django.contrib import admin
from library.models import Usuario, Autor, Genero, Editorial, Idioma, Libro, Prestamo, Perfil

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Libro)
admin.site.register(Prestamo)

class AdminUsuario(admin.ModelAdmin):
    list_display=('username','email','nombres','usuario_activo','usuario_administrador')
    search_fields=('username','email','nombres')
    list_filter=['usuario_activo']

admin.site.register(Usuario,AdminUsuario)
admin.site.register(Perfil)
