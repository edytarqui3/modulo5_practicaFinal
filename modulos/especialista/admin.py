import csv
from django.contrib import admin
from datetime import datetime as dt
from django.http import HttpResponse
from easy_select2 import select2_modelform

from .models import (
    Especialidad,
    Medico,
)

MedicoForm = select2_modelform(Medico, attrs={'width': '400px'})


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('especialidad', 'descripcion', 'fecha_creacion', 'usuario_creacion',)
    search_fields = ('especialidad', 'descripcion', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(MedicoAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    form = MedicoForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('medico', 'especialidad', 'nombre', 'imagen_tag', 'ci', 'telefono', 'estado', 'fecha_creacion',
                    'usuario_creacion',)
    search_fields = ('especialidad', 'medico', 'descripcion', 'ci',)
    readonly_fields = ('imagen_preview',)

    def imagen_preview(self, obj):
        return obj.imagen_preview

    def imagen_tag(self, obj):                                                                                                                                                 
        return obj.imagen_tag

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(MedicoAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset

    actions = ['export_a_csv', ]
