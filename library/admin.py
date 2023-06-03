from django.contrib import admin
from library.models import Usuario, Autor, Genero, Editorial, Idioma, Libro, Prestamo, Perfil

# Register your models here.
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Idioma)

class AdminLibro(admin.ModelAdmin):
    list_display=('id_libro','titulo','isbn','idioma_id','cantidad_copias','disponibilidad')
    search_fields=('id_libro','autor_id','genero_id','idioma_id','genero_id')
    list_filter=['genero_id','disponibilidad','autor_id','idioma_id']
admin.site.register(Libro,AdminLibro)

class AdminPrestamo(admin.ModelAdmin):
    list_display=('id_prestamo','libro_id','usuario_id','fecha_salida','fecha_entrada','comentario')
    search_fields=('usuario_id','libro_id','fecha_salida','id_prestamo')
admin.site.register(Prestamo,AdminPrestamo)

class AdminUsuario(admin.ModelAdmin):
    list_display=('username','email','nombres','usuario_activo','usuario_administrador')
    search_fields=('username','email','nombres')
    list_filter=['usuario_activo']
admin.site.register(Usuario,AdminUsuario)

class AdminPerfil(admin.ModelAdmin):
    list_display=('usuario','apellidos','telefono','direccion')
    search_fields=('usuario','apellidos','telefono')
admin.site.register(Perfil,AdminPerfil)
