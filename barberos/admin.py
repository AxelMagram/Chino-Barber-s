from django.contrib import admin

from .models import Barbero


@admin.register(Barbero)
class BarberoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'user', 'activo')
    list_filter = ('activo',)
    search_fields = ('nombre', 'telefono')
