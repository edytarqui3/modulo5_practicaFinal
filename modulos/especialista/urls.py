from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadViewsets,
    MedicoViewsets
)

api_router = DefaultRouter()

api_router.register('especialidad', EspecialidadViewsets, 'especialidad')
api_router.register('medico', MedicoViewsets, 'medico')

urlpatterns = api_router.urls
