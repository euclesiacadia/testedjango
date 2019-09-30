from django.shortcuts import render,redirect
from eteam.models import Pessoa
from eteam.models import Equipa
from website.forms import CadastrarPessoaForm, CriarEquipaForm, AdicionarMembrosForm

# Create your views here.
def index(request):
    return render(request,'website/index.html',{})

def lista_pessoas(request):
    pessoas = Pessoa.objectos.all()
    return render(request,'website/listar-pessoas.html',{'pessoas':pessoas})
    
def cadastra_pessoa(request):
    form = CadastrarPessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('website:lista_pessoas')
    return render(request,'website/cadastrar-pessoa.html',{'form': form})

def cria_equipa(request):
    form = CriarEquipaForm(request.POST or None)
    equipa = Equipa.objectos.all()
    if form.is_valid():
        form.save()
        return redirect('website:adiciona_membros', equipa=equipa.pk)

def adiciona_membros(request, pk):
    form = AdicionarMembrosForm(request.POST )
    if form.is_valid():
        form.save()
        return redirect('lista_membros')


