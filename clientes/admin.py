from django.contrib import admin

from .models import Cliente, Servicio, Turno, Notificacion, ImagenGaleria


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'creado')
    search_fields = ('nombre', 'telefono', 'email')


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion_minutos', 'precio', 'requiere_confirmacion', 'activo')
    list_filter = ('activo', 'requiere_confirmacion')


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'hora_inicio', 'hora_fin', 'cliente', 'barbero', 'servicio', 'estado')
    list_filter = ('estado', 'barbero', 'servicio', 'fecha')
    search_fields = ('cliente__nombre', 'cliente__telefono')
    date_hierarchy = 'fecha'


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('turno', 'canal', 'estado', 'programada_para', 'enviada_en')
    list_filter = ('canal', 'estado')


@admin.register(ImagenGaleria)
class ImagenGaleriaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'titulo', 'orden', 'activo')
    list_editable = ('orden', 'activo')
