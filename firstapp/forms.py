from django.forms import ModelForm

from .models import Cadastro_Clientes


class UpdateForm(ModelForm):
    class Meta:
        model = Cadastro_Clientes
        fields = ['nome', 'email', 'numero_celular', 'cidade']
