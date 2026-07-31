from django.db import models
from django.contrib.auth.models import User


class Barbero(models.Model):
    """Perfil de un barbero, vinculado a un usuario de Django para el login."""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='barbero'
    )
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=True)
    foto = models.ImageField(upload_to='barberos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Barbero'
        verbose_name_plural = 'Barberos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
