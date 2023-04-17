from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    preco = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Preço")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
