from django.urls import path

from . import views

urlpatterns = [
    path('', views.pagina_inicial),
    path('submit/', views.submit_post),
    path('edit/<int:pk>/', views.edit_post, name='url_update'),
    path('delete/<int:id_cadastro>/', views.delete_cadastro),
    path('teste/', views.pagina_teste),
]
