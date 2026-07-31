from datetime import datetime, timedelta

from django.db import models


class Cliente(models.Model):
    """Cliente que reserva turnos. No tiene login (según requisitos)."""
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.telefono})'


class Servicio(models.Model):
    """Servicio ofrecido: corte, tintura, afeitado."""
    nombre = models.CharField(max_length=80)
    duracion_minutos = models.PositiveIntegerField(
        help_text='Duración del servicio en minutos.'
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    requiere_confirmacion = models.BooleanField(
        default=False,
        help_text='Ej: la tintura requiere confirmación previa del barbero.',
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.duracion_minutos} min)'


class Turno(models.Model):
    """Reserva de un cliente con un barbero para un servicio."""

    class Estado(models.TextChoices):
        PENDIENTE = 'PEN', 'Pendiente'
        CONFIRMADO = 'CON', 'Confirmado'
        RECHAZADO = 'REC', 'Rechazado'
        CANCELADO = 'CAN', 'Cancelado'
        COMPLETADO = 'COM', 'Completado'

    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='turnos'
    )
    barbero = models.ForeignKey(
        'barberos.Barbero', on_delete=models.CASCADE, related_name='turnos'
    )
    servicio = models.ForeignKey(
        Servicio, on_delete=models.PROTECT, related_name='turnos'
    )
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField(blank=True)
    estado = models.CharField(
        max_length=3, choices=Estado.choices, default=Estado.PENDIENTE
    )
    notas = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['fecha', 'hora_inicio']
        constraints = [
            models.UniqueConstraint(
                fields=['barbero', 'fecha', 'hora_inicio'],
                name='unico_turno_barbero_horario',
            )
        ]

    def save(self, *args, **kwargs):
        # Calcula automáticamente la hora de fin según la duración del servicio.
        if self.hora_inicio and self.servicio_id:
            inicio = datetime.combine(self.fecha, self.hora_inicio)
            fin = inicio + timedelta(minutes=self.servicio.duracion_minutos)
            self.hora_fin = fin.time()
        super().save(*args, **kwargs)

    @property
    def es_ingreso(self):
        """Cuenta como ingreso solo si el turno fue completado."""
        return self.estado == self.Estado.COMPLETADO

    def __str__(self):
        return f'{self.fecha} {self.hora_inicio} · {self.cliente} con {self.barbero}'


class Notificacion(models.Model):
    """Aviso al cliente por SMS o push (recordatorio 2h antes, confirmación, cambios)."""

    class Canal(models.TextChoices):
        SMS = 'SMS', 'SMS'
        PUSH = 'PUSH', 'Notificación push'

    class Estado(models.TextChoices):
        PROGRAMADA = 'PRO', 'Programada'
        ENVIADA = 'ENV', 'Enviada'
        FALLIDA = 'FAL', 'Fallida'

    turno = models.ForeignKey(
        Turno, on_delete=models.CASCADE, related_name='notificaciones'
    )
    canal = models.CharField(max_length=4, choices=Canal.choices)
    mensaje = models.CharField(max_length=300)
    programada_para = models.DateTimeField()
    enviada_en = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=3, choices=Estado.choices, default=Estado.PROGRAMADA
    )

    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['programada_para']

    def __str__(self):
        return f'{self.get_canal_display()} → {self.turno} ({self.get_estado_display()})'


class ImagenGaleria(models.Model):
    """Imágenes de cortes para la galería del hero en la página de inicio."""
    titulo = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='galeria/')
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Imagen de galería'
        verbose_name_plural = 'Galería'
        ordering = ['orden']

    def __str__(self):
        return self.titulo or f'Imagen #{self.pk}'
