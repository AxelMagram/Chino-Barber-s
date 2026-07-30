from django.urls import path
from . import views

app_name = 'barberos'

urlpatterns = [
    # La autenticación y el dashboard se implementan en el Paso 3 y 6.
    path('acceso/', views.placeholder_login, name='login'),
    path('dashboard/', views.placeholder_dashboard, name='dashboard'),
]
