from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from eteam.models import Pessoa
from eteam.models import Equipa
from website.forms import RegistarPessoaForm, CriarEquipaForm, AdicionarMembrosForm

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "website/index.html"

class PessoaListView(ListView):
    template_name = "website/listar_pessoas.html"
    model = Pessoa
    context_object_name = "pessoas"

class PessoaCreateView(CreateView):
    template_name = "website/criar_pessoa.html"
    model = Pessoa
    form_class = RegistarPessoaForm
    success_url = reverse_lazy("website:lista_pessoas")

class EquipaListView(ListView):
    template_name = 'lista_equipas.html'
    model = Pessoa
    context_object_name = "equipas"

class EquipaCreateView(CreateView):
    template_name = 'website/criar_equipa.html'
    model = Equipa
    form_class = CriarEquipaForm
    success_url = reverse_lazy("website:lista_equipas")

#esta view serve para adicionar os membros a equipa
class MembrosCreateView(CreateView):
    template_name = 'website/adicionar.html'
    model = Pessoa
    form_class = AdicionarMembrosForm
    success_url = reverse_lazy("website:lista_membros")

class MembrosDeleteView(DeleteView):
    template_name = "website/remover.html"
    model = Pessoa
    context_object_name = 'pessoa'
    success_url = reverse_lazy("website:lista_pessoas")


'''
def lista_pessoas(request):
    pessoas = Pessoa.objectos.all()
    return render(request,"listar_pessoas.html",{'pessoas':pessoas})
    
def cria_pessoa(request):
    form = RegistarPessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pessoas')
    return render(request,'c')
    
def lista_pessoas(request):
'''