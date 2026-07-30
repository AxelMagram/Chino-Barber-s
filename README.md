# Chino Barber — Sistema de Gestión de Turnos

Plataforma web para reservar turnos de barbería (clientes) y gestionar agenda,
turnos y métricas (barberos).

## Stack

- **Backend:** Python 3.10+ / Django 5.2
- **Frontend:** Tailwind CSS (vía CDN, sin build)
- **Base de datos:** SQLite

## Estructura

```
config/       Configuración del proyecto (settings, urls)
clientes/     App pública: inicio, reservas, servicios
barberos/     App privada: login, dashboard, gestión de turnos, métricas
templates/    Plantillas HTML (base + por app)
static/       Archivos estáticos
media/        Imágenes subidas (galería, etc.)
```

## Puesta en marcha

```bash
# 1. (Recomendado) crear entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Migrar la base de datos
python manage.py migrate

# 4. Crear un usuario administrador (opcional, para el panel /admin)
python manage.py createsuperuser

# 5. Levantar el servidor de desarrollo
python manage.py runserver
```

La app queda disponible en http://127.0.0.1:8000/

## Estado del desarrollo

- [x] Paso 1 — Configuración inicial del proyecto
- [ ] Paso 2 — Modelos de datos
- [ ] Paso 3 — Autenticación de barberos
- [ ] Paso 4 — Página de cliente
- [ ] Paso 5 — Flujo y lógica de reservas
- [ ] Paso 6 — Dashboard del barbero (gestión de turnos)
- [ ] Paso 7 — Métricas y gráficos
- [ ] Paso 8 — Exportación de reportes (PDF / Excel)
- [ ] Paso 9 — Notificaciones (SMS + push)
- [ ] Paso 10 — Pruebas y verificación

## Notas de seguridad

- El `SECRET_KEY` de Django y las credenciales de SMS deben ir en un archivo
  `.env` (ya ignorado por git), **nunca** commiteados al repositorio.
- `DEBUG = True` es solo para desarrollo; en producción debe ser `False`.
