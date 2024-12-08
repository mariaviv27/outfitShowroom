from django.db import models

class Estilo(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
 
class Ocasion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
 
class Outfit(models.Model):
    # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estilo = models.ForeignKey(Estilo, on_delete=models.CASCADE)
    ocasion = models.ManyToManyField(Ocasion)
    #foto = models.ImageField(upload_to='static/media/outfits/', null=True, blank=True)
    foto = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=100)  # Nombre de quien comenta
    puntuacion = models.PositiveSmallIntegerField()  # Puntuación de 1 a 5
    texto = models.TextField(blank=True, null=True)  # Texto opcional del comentario
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha del comentario

    def __str__(self):
        return f"{self.nombre} - {self.puntuacion} estrellas"
