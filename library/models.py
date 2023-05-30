from django.db import models

# Create your models here.
class Lector(models.Model):
    id_lector = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False)
    telefono = models.CharField(max_length=9, null=False)
    direccion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre +" "+self.apellido

class Autor(models.Model):
    id_autor = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    id_genero = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    id_editorial = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200, null=False)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    id_idioma = models.BigAutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_libro = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=250, null=False)
    fecha_lanzamiento = models.DateField(null=False, blank=False)
    autor_id = models.ManyToManyField(Autor)
    genero_id = models.ManyToManyField(Genero)
    editorial_id = models.ForeignKey(Editorial, on_delete=models.DO_NOTHING)
    isbn = models.CharField('ISBN',max_length=13, null=False, blank=False)
    paginas = models.PositiveIntegerField(null=False, blank=False)
    idioma_id = models.ForeignKey(Idioma, null=False, blank=False, on_delete=models.DO_NOTHING)
    cantidad_copias = models.PositiveIntegerField('número de copias', default=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    portada = models.ImageField(upload_to='books/covers/', max_length=254)
    disponibilidad = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, null=False, blank=False)
    lector_id = models.ForeignKey(Lector, null=False, blank=False, on_delete=models.CASCADE)
    libro_id = models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
    fecha_salida = models.DateField(auto_now_add=True, null=False, blank=False)
    fecha_entrada = models.DateField('Posible fecha de ingreso',blank=True, null=True)
    comentario = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'
        ordering = ['fecha_salida']

    def __str__(self):
        fecha = str(self.fecha_salida)
        return str(self.libro_id.titulo+" "+fecha+" "+self.lector_id.nombre)
