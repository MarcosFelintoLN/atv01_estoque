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

def listar(request):
    template_name = "estoque/mostrar_produto.html"
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, template_name, context)