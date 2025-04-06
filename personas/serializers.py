from rest_framework import serializers
from .models import Empresa, Persona

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['numero_documento', 'primer_nombre', 'primer_apellido', 'correo_electronico', 'telefono_celular'] # Ajusta los campos que quieras mostrar

class EmpresaListSerializer(serializers.ModelSerializer):
    representante_legal = PersonaSerializer()  # Aquí incluimos la relación con la persona

    class Meta:
        model = Empresa
        fields = ['id', 'razon_social', 'tipo_empresa', 'correo_electronico', 'numero_celular', 'representante_legal']