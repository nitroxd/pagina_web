from django import admin
from django.http import HttpResponse


def volver(request):
	return HttpResponse("hola mundo")