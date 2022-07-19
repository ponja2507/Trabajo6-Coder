from django.urls import path

from AppTrabajo.views import familia, familiar

urlpatterns = [
    path('familiar/<nombre>/<edad>/<nacimiento>', familiar),
    path('lista-familia', familia),
]
