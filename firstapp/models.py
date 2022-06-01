from django.db import models


class Cadastro_Clientes(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    numero_celular = models.CharField(max_length=11)
    cidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    def get_nome_cliente(self):
        return self.nome
