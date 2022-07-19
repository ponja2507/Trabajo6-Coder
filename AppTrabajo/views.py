from django.http import HttpResponse
from django.shortcuts import render

from AppTrabajo.models import Familiar

# Create your views here.
def familiar(self, nombre, edad, nacimiento):

    familiar1 = Familiar(nombre = nombre, edad = edad, nacimiento = nacimiento)
    familiar1.save()
    texto = f"Nombre: {familiar1.nombre} Edad: {familiar1.edad} Nacimiento: {familiar1.nacimiento}"

    return HttpResponse(texto)

def familia(self):
    lista = Familiar.objects.all()

    return render(self, "familia.html", {"familia":lista})

