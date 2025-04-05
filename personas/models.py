from django.db import models

# personas/models.py

from django.db import models

class Persona(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
    ("CC", "Cédula de Ciudadanía"),
    ("CE", "Cédula de Extranjería"),
    ("NR", "Nombre Regional"),
    ("NUIP", "NUIP"),
    ("PAS", "Pasaporte"),
    ("PEP", "Permiso Especial de Permanencia"),
    ("RC", "Registro Civil"),
    ("TI", "Tarjeta de Identidad"),
    ("TP", "Tarjeta Prueba"),
    ("NIT", "NIT"),  # Agregado
]


    tipo_documento = models.CharField(max_length=10, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=20, primary_key=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    correo_electronico = models.EmailField()
    telefono_celular = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}".strip()


class Empresa(models.Model):
    TIPO_EMPRESA_CHOICES = [
        ('comercializador', 'Comercializador'),
        ('transformador', 'Transformador'),
        ('exportador', 'Exportador'),
    ]

    NATURALEZA_EMPRESA_CHOICES = [
        ('privada', 'Privada'),
        ('publica', 'Pública'),
        ('mixta', 'Mixta'),
    ]

    pais = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    digito_verificacion = models.CharField(max_length=5)
    razon_social = models.CharField(max_length=255)
    nombre_comercial = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    tipo_empresa = models.CharField(max_length=20, choices=TIPO_EMPRESA_CHOICES)
    naturaleza_empresa = models.CharField(max_length=10, choices=NATURALEZA_EMPRESA_CHOICES)
    correo_electronico = models.EmailField()
    numero_celular = models.CharField(max_length=15)
    quien_diligencia = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    area = models.CharField(max_length=100)

    representante_legal = models.ForeignKey(
        Persona,
        on_delete=models.PROTECT,
        to_field='numero_documento',
        related_name='empresas_representadas'
    )

    def __str__(self):
        return self.razon_social

