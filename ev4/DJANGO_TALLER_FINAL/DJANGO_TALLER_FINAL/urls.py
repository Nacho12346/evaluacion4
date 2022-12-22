"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from startapp import views

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.index),
    path('inscripciones/', views.listar),
    path('agregarinscripcion', views.agregar),
    path('eliminar/<int:id>', views.eliminar),
    path('actualizar/<int:id>', views.actualiza),

    path('inscritosApi/', views.Api),

    path('inscritosCBV/', views.ListarCBV.as_view()),
    path('inscritosCBV/<int:pk>', views.DetalleCBV.as_view()),

    path('inscritosFBV/', views.ListarFBV),
    path('inscritosFBV/<int:pk>', views.DetalleFBV),
]
