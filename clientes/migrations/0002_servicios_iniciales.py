from django.db import migrations


def crear_servicios(apps, schema_editor):
    Servicio = apps.get_model('clientes', 'Servicio')
    servicios = [
        # (nombre, duracion_min, precio_placeholder, requiere_confirmacion)
        ('Corte de cabello', 30, 5000, False),
        ('Tintura', 90, 15000, True),   # requiere confirmación previa del barbero
        ('Afeitado', 30, 4000, False),
    ]
    for nombre, dur, precio, requiere in servicios:
        Servicio.objects.get_or_create(
            nombre=nombre,
            defaults={
                'duracion_minutos': dur,
                'precio': precio,
                'requiere_confirmacion': requiere,
                'activo': True,
            },
        )


def borrar_servicios(apps, schema_editor):
    Servicio = apps.get_model('clientes', 'Servicio')
    Servicio.objects.filter(
        nombre__in=['Corte de cabello', 'Tintura', 'Afeitado']
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(crear_servicios, borrar_servicios),
    ]
