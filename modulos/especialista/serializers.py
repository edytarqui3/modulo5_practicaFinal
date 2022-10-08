from rest_framework import serializers
from .models import (
    Especialidad
)

class EspecialidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'especialidad', 'descripcion', )


class MedicoSerializers(serializers.ModelSerializer):
    especialidad = EspecialidadSerializers(read_only=True)
    especialidad_id = serializers.IntegerField()
    
    class Meta:
        model = Especialidad
        fields = (
            'id', 'especialidad', 'especialidad_id',
            'nombre','ci', 'descripcion', 'foto', 'telefono', 'estado'
        )
