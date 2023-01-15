from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    grado = models.IntegerField(default=14)

    def __str__(self):
        return f"{self.nombre}, {self.grado}"
    

    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField
    edad = models.IntegerField(default=14)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

        
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
 

class Trabajo(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}, {self.entregado}"

class Pais(models.Model):
    pais = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)

class Entrada(models.Model):
    nombre = models.CharField(max_length=30)
    contenido = models.CharField(max_length=30)
    imagen = models.URLField()
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=60)
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre




