from django.shortcuts import render, redirect
from .forms import *

def cadastrar(request):
    template_name = "estoque/cadastrar_produto.html"
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        
            return redirect('index.html')
        
    else:
        form = ProdutoForm()

    return render(request, template_name, {"form":form})