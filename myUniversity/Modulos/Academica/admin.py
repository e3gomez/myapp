from django.contrib import admin
from Modulos.Academica.models import *
# Register your models here.
 admin.site.Register(Carrera)
 admin.site.Register(Estudiante)
 admin.site.Register(Curso)
 admin.site.Register(Matricula) 