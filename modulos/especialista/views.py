from modulos.logmodel.viewsets import RestLogModelViewSet
from .models import (
    Especialidad,
    Medico
)
from .serializers import (
    EspecialidadSerializers,
    MedicoSerializers
)


class EspecialidadViewsets(RestLogModelViewSet):
    model = Especialidad
    serializer_class = EspecialidadSerializers
    queryset = Especialidad.objects.filter(fecha_eliminacion__isnull=True)


class MedicoViewsets(RestLogModelViewSet):
    model = Medico
    serializer_class = MedicoSerializers
    queryset = Medico.objects.filter(fecha_eliminacion__isnull=True)
