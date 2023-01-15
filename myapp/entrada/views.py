from django.shortcuts import render


def home(request):
    Entrada = Entrada.objects.all()
    return render(request,"bienvenida.html",{"Entrada":Entrada})
