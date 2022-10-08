from django.db import models
from modulos.logmodel.models import LogModel
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from .validators import (
    validar_costo_producto,
    validar_stock_minimo
)


class Especialidad(LogModel):
    especialidad = models.CharField('Especialidad', max_length=50, unique=True)
    descripcion = models.TextField('Descripcion')

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.especialidad

class Medico(LogModel):
    especialidad = models.ForeignKey(Especialidad, related_name='+', on_delete=models.PROTECT)
    nombres = models.CharField('Nombre del Medico', max_length=100, blank=False, null=False)
    ci = models.CharField('Numero de C.I.', max_length=100, blank=False, null=False)
    descripcion = models.TextField('Descripción')
    foto = models.ImageField('Imagen del medico', upload_to='medicos/', blank=False, null=False)
    telefono = models.IntegerField('telefono', default=0, validators=[validar_stock_minimo, ])
    estado = models.BooleanField('Estado Actual', default=True)

    @property
    def imagen_preview(self):
        if self.imagen:
            _imagen = get_thumbnail(self.foto, '200x200', upscale=False, crop=False, quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_imagen.url,
                                                                              _imagen.width,
                                                                              _imagen.height))
        return ""

    @property
    def imagen_tag(self):
        if self.imagen:
            _imagen = get_thumbnail(self.foto, '55x55', upscale=False, crop=False, quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_imagen.url,
                                                                              _imagen.width,
                                                                              _imagen.height))
        return ""

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return f'{self.producto} ( {self.especialidad})'
