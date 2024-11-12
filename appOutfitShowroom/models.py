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
    foto = models.ImageField(upload_to='\static\layout\images\outfits', null=True, blank=True)
    def __str__(self):
        return self.nombre