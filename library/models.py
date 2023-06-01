from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        user = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,nombres,password):
        user = self.create_user(
            username = username, 
            email = email, 
            nombres = nombres,
            password = password
        )
        user.usuario_administrador = True
        user.save()
        return user


class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario',unique= True, max_length=100)
    email = models.EmailField('Correo electrónico', max_length=254, unique= True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', blank=True) #para roles
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres']

    def __str__(self):
        return f'{self.nombres}'
    
    def has_perm(self,perm,obj = None):
       return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil', verbose_name='Usuario')
    apellidos = models.CharField('Apellidos', max_length=254, blank=True, null=True)
    imagen = models.ImageField('Imágen de perfil', upload_to='users/profilepics/', max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=9, null=False)
    direccion = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.usuario.username
    
    def create_usuario_perfil(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(usuario=instance)

    def save_usuario_perfil(sender, instance, **kwargs):
        instance.perfil.save()

    post_save.connect(create_usuario_perfil, sender=Usuario)
    post_save.connect(save_usuario_perfil, sender=Usuario)

class Autor(models.Model):
    id_autor = models.BigAutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    id_genero = models.BigAutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    id_editorial = models.BigAutoField('ID', primary_key=True)
    nombre = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    id_idioma = models.BigAutoField('ID', primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_libro = models.BigAutoField('ID', primary_key=True)
    titulo = models.CharField('Título de libro', max_length=250, null=False)
    fecha_lanzamiento = models.DateField('Fecha de lanzamiento',null=False, blank=False)
    autor_id = models.ManyToManyField(Autor)
    genero_id = models.ManyToManyField(Genero)
    editorial_id = models.ForeignKey(Editorial, on_delete=models.DO_NOTHING)
    isbn = models.CharField('ISBN',max_length=13, null=False, blank=False)
    paginas = models.PositiveIntegerField('Número de páginas', null=False, blank=False)
    idioma_id = models.ForeignKey(Idioma, null=False, blank=False, on_delete=models.DO_NOTHING)
    cantidad_copias = models.PositiveIntegerField('número de copias', default=100, null=False, blank=False)
    descripcion = models.TextField('Descripción', null=False, blank=False)
    portada = models.ImageField(upload_to='books/covers/', max_length=254)
    disponibilidad = models.BooleanField('Disponible/No disponible', default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    id_prestamo = models.AutoField('ID', primary_key=True, null=False, blank=False)
    usuario_id = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    libro_id = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    fecha_salida = models.DateField('Fecha de préstamo', auto_now_add=True, null=False, blank=False)
    fecha_entrada = models.DateField('Posible fecha de ingreso',blank=True, null=True)
    comentario = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        ordering = ['fecha_salida']

    def __str__(self):
        fecha = str(self.fecha_salida)
        return str(self.libro_id.titulo+" "+fecha+" "+self.lector_id.nombre)
