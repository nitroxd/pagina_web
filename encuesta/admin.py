from django.contrib import admin
from encuesta.models import pregunta,campo


class admink(admin.ModelAdmin):


	fieldsets=[('Pregunta integral',{'fields':['pregunta1']}),
				('fecha horaria',{'fields':['fecha']}),]

admin.site.register(pregunta,admink)

# Register your models here.
