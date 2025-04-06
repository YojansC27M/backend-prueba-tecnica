# Proyecto de Backend y Frontend - Empresa

## Descripción

Este proyecto consiste en un backend desarrollado en **Django** utilizando **PostgreSQL** como base de datos, y un frontend desarrollado en **Next.js** con **Material UI**, **SweetAlert2**, y **Axios** para la interacción con el backend.

## Backend

### Tecnologías

- **Django**: Framework para el desarrollo del backend en Python.
- **PostgreSQL**: Sistema de gestión de bases de datos relacional utilizado.
- **Django REST Framework**: Para la creación de APIs RESTful.
- **psycopg2**: Adaptador de PostgreSQL para Django.
  
### Requisitos

- Python 3.x
- PostgreSQL 12 o superior

### Instalación

1. Ingresar a la carpeta del proyecto django:

   ```bash
   
   cd <nombre_del_directorio_backend>
   ```

2. Crea un entorno virtual e instálalo en el entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install Django
   pip install django djangorestframework psycopg2-binary


   ```

4. Configura la base de datos en `settings.py`:

   Asegúrate de tener configurado PostgreSQL correctamente en el archivo `settings.py` de Django:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nombre_de_la_base_de_datos',
           'USER': 'usuario',
           'PASSWORD': 'contraseña',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

### Endpoints

- **POST /api/crear-empresa/**: Endpoint para crear una nueva empresa.
- **GET /api/verificar-persona/**: Endpoint para verificar si una persona existe, dado su tipo y número de documento.