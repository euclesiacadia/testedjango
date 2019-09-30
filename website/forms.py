from django import forms
from eteam.models import Pessoa, Equipa

class CadastrarPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'apelido', 'cargo']

class CriarEquipaForm(forms.ModelForm):
    class Meta:
        model = Equipa
        fields = ['nome']


class AdicionarMembrosForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['equipa']

class RemoverMembros(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['equipa']

class ListarMembros(forms.ModelForm):
    class Meta:
        model = Equipa
