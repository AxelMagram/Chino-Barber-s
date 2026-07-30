from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
]
