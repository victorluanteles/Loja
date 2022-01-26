from django.urls import path
from inter import views
urlpatterns = [
    path('inicio/', views.inicioLoja, name='inicio'),
    path('inicio2/', views.inicioLoja2, name='inicio2'),
]