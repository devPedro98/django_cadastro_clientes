from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial),
    path('teste/', views.pagina_teste),
]
