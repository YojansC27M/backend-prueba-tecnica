from venv import logger
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .serializers import EmpresaListSerializer
from .models import Persona, Empresa


@api_view(['GET'])
def verificar_persona(request):
    tipo_documento = request.query_params.get('tipo_documento')
    numero_documento = request.query_params.get('numero_documento')

    if not tipo_documento or not numero_documento:
        return Response({'error': 'Datos incompletos'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        persona = Persona.objects.get(tipo_documento=tipo_documento, numero_documento=numero_documento)
        return Response({'existe': True, 'nombres': f'{persona.primer_nombre} {persona.segundo_nombre} {persona.primer_apellido} {persona.segundo_apellido}'})
    except Persona.DoesNotExist:
        return Response({'existe': False})


@api_view(['POST'])
def crear_empresa(request):
    # Extraer los datos del body del request
    data = request.data

    # Validar que los campos obligatorios estén presentes
    required_fields = [
        "pais", "departamento", "municipio", "digito_verificacion",
        "direccion", "correo_electronico", "numero_celular", "quien_diligencia",
        "cargo", "area", "representante_legal"
    ]
    
    for field in required_fields:
        if field not in data:
            return Response({'error': f'{field} es obligatorio'}, status=status.HTTP_400_BAD_REQUEST)

    # Obtener el número de documento del representante legal
    numero_documento = data["representante_legal"]

    # Verificar si la persona existe en la base de datos con el número de documento
    try:
        persona = Persona.objects.get(numero_documento=numero_documento)
    except Persona.DoesNotExist:
        return Response({'error': 'Representante legal no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    # Crear la empresa con los datos proporcionados
    empresa_data = {
        "pais": data["pais"],
        "departamento": data["departamento"],
        "municipio": data["municipio"],
        "digito_verificacion": data["digito_verificacion"],
        "razon_social": data.get("razon_social", ""),  # Opcional
        "nombre_comercial": data.get("nombre_comercial", ""),  # Opcional
        "direccion": data["direccion"],
        "tipo_empresa": data["tipo_empresa"],
        "naturaleza_empresa": data["naturaleza_empresa"],
        "correo_electronico": data["correo_electronico"],
        "numero_celular": data["numero_celular"],
        "quien_diligencia": data["quien_diligencia"],
        "cargo": data["cargo"],
        "area": data["area"],
        "representante_legal": persona,
    }

    empresa = Empresa.objects.create(**empresa_data)

    return Response({"message": "Empresa creada exitosamente", "empresa_id": empresa.id}, status=status.HTTP_201_CREATED)
  
from rest_framework import status
from rest_framework.response import Response
from .models import Persona

@api_view(['POST'])
def crear_persona(request):
    # Extraer los datos del cuerpo del request
    data = request.data

    # Validar que todos los campos requeridos estén presentes
    required_fields = [
        "tipo_documento", "numero_documento", "primer_nombre", "primer_apellido", 
        "correo_electronico", "telefono_celular", "direccion"
    ]
    
    for field in required_fields:
        if field not in data:
            return Response({'error': f'{field} es obligatorio'}, status=status.HTTP_400_BAD_REQUEST)

    # Crear la persona con los datos proporcionados
    try:
        persona = Persona.objects.create(
            tipo_documento=data["tipo_documento"],
            numero_documento=data["numero_documento"],
            primer_nombre=data["primer_nombre"],
            segundo_nombre=data.get("segundo_nombre", ""),  # Opcional
            primer_apellido=data["primer_apellido"],
            segundo_apellido=data.get("segundo_apellido", ""),  # Opcional
            correo_electronico=data["correo_electronico"],
            telefono_celular=data["telefono_celular"],
            direccion=data["direccion"]
        )
        return Response({"message": "Persona creada exitosamente", "persona_id": persona.numero_documento}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def listar_empresas(request):
    try:
        # Intentamos obtener todas las empresas
        empresas = Empresa.objects.all()

        # Si no hay empresas, lanzamos un error de tipo 404
        if not empresas:
            logger.warning("No se encontraron empresas.")
            return Response({"detail": "No se encontraron empresas."}, status=status.HTTP_404_NOT_FOUND)

        # Serializamos los datos de las empresas
        serializer = EmpresaListSerializer(empresas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        # Capturamos cualquier excepción que ocurra y la registramos
        logger.error(f"Error al listar empresas: {str(e)}")
        
        # Devolvemos un error genérico 500 en caso de fallo
        return Response({"error": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
class EliminarEmpresaView(APIView):
 def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
            empresa.delete()  # Eliminar la empresa
            return Response({"detail": "Empresa eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)
        except Empresa.DoesNotExist:
            raise NotFound("Empresa no encontrada.")
