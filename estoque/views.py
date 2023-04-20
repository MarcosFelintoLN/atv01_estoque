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
    template_name = "estoque/index.html"
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, template_name, context)

def excluir(request, pk):
    produto_escolhido = Produto.objects.get(pk=pk)
    produto_escolhido.delete()
    return redirect('index.html')

def editar(request, pk):
    template_name = "estoque/cadastrar_produto.html"
    editar_produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=editar_produto)
        if form.is_valid():
            editar_produto = form.save()
            editar_produto.nome = form.data['nome']
            editar_produto.preco = form.data['preco']
            editar_produto.descricao = form.data['descricao']
            editar_produto.quantidade = form.data['quantidade']
            editar_produto.save()
            return redirect('index.html')
    else:
        form = ProdutoForm(instance=editar_produto)
    return render(request,template_name,{'form':form})