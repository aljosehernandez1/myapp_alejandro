from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime
from django.db import models
from appcoder.models import Entrada, Comentario, Estudiante, Profesor, Curso, Trabajo




def about(request):
    return HttpResponse('About')

def saludar(request):
    return render(request,"bienvenida.html")

def acerca(request):
    return render(request,"Acerca_de.html")

def home(request):
    articulos = Entrada.objects.all()
    if request.method == "POST":
        nombre = request.POST["nombre"]
        mensaje = request.POST["mensaje"]
        p = Comentario(nombre=nombre, comentario=mensaje)
        p.save()
        mensaje ="Gracias por tu comentario"
        return render(request,"bienvenida.html",{"articulos":articulos,"mensaje":mensaje})
    return render(request,"bienvenida.html",{"articulos":articulos})


def cursos(request):
    return render(request,"cursos.html")

def listar_estudiantes(request):
    contexto ={
        'estudiante': Estudiante.objects.all()
    }

    return render(
            request=request,
            template_name='estudiante.html',
            context=contexto
            )

def listar_profesores(request):
    contexto ={
        'profesor': Profesor.objects.all()
    }

    return render(
            request=request,
            template_name='profesor.html',
            context=contexto
            )

def listar_cursos(request):
    contexto ={
        'cursos': Curso.objects.all()
    }

    return render(
            request=request,
            template_name='cursos.html',
            context=contexto
            )


def listar_trabajos(request):
    contexto ={
        'trabajo': Trabajo.objects.all()
    }

    return render(
            request=request,
            template_name='trabajos.html',
            context=contexto
            )

def crear_curso(request):
    if request.method =="POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], grado=data['grado'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:
        return render(
            request=request,
            template_name='formulario_curso.html'
        ) 

