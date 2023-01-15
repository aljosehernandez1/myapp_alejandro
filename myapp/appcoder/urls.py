from django.urls import path
from . import views
from appcoder import views
from appcoder.views import ( listar_estudiantes, listar_profesores, listar_cursos, listar_trabajos, 
 crear_curso)


urlpatterns = [
    path('about/', views.about),
    path('saludar/',views.saludar),
    path('acerca/',views.acerca),   
    path('',views.home),
    path('',views.acerca),
    path('cursos',views.cursos),   
    path('estudiante', listar_estudiantes, name="listar_estudiantes"),
    path('profesores', listar_profesores, name="listar_profesores"),
    path('trabajos', listar_trabajos, name="listar_trabajos"),
    path('cursos', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
   ]
