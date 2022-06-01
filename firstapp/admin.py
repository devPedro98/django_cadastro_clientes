from django.contrib import admin

from firstapp.models import Cadastro_Clientes


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'numero_celular', 'cidade')


admin.site.register(Cadastro_Clientes, CadastroAdmin)
