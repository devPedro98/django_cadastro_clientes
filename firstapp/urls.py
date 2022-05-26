from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial),
    path('submit/', views.submit_post),
    path('teste/', views.pagina_teste),
]
