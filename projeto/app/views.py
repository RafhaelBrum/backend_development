from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Pagina, Produto
from .forms import TopicoForm, ProdutoForm

def index(request):
    return render(request, 'index.html')

def help(request):
    return render(request, 'help.html')

def calculadora(request):
    return render(request, 'calculadora.html')

def helloworld(request):
    return render(request, 'helloworld.html')

class PaginaListView(ListView):
    template_name = 'pagina_list.html' 
    context_object_name = 'paginas'

    def get_queryset(self):
        return Pagina.objects.all().prefetch_related('registroacesso_set')
    
def criar_topico(request):
    if request.method == 'POST':
        form = TopicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina-list')
    else:
        form = TopicoForm()
    
    return render(request, 'criar_topico.html', {'form': form})


def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista-produtos')  
    else:
        print("Erro. Campos Invalidos")
        form = ProdutoForm()
    
    return render(request, 'criar_produto.html', {'form': form})


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})