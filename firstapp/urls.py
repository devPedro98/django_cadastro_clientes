from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial),
    path('submit/', views.submit_post),
    path('edit/id=<int:id_cadastro>/', views.edit_post),
    path('delete/<int:id_cadastro>/', views.delete_cadastro),
    path('teste/', views.pagina_teste),
]
