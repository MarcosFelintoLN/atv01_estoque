from django import forms
from django.forms import ModelForm
from .models import *

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','descricao','quantidade']