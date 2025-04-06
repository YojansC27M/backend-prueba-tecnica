"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from personas import views  # ✅ Esto busca views en la app personas
from personas.views import EliminarEmpresaView  # Importar la vista de eliminación

urlpatterns = [
    path('api/verificar-persona/', views.verificar_persona, name='verificar_persona'),
    path('api/crear-empresa/', views.crear_empresa, name='crear_empresa'),
    path('api/crear-persona/', views.crear_persona, name='crear_persona'),
    path('api/listar-empresas/', views.listar_empresas, name='listar_empresas'),
    path('api/eliminar-empresa/<int:pk>/', EliminarEmpresaView.as_view(), name='delete'),
]
