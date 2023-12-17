from django import forms
from .models import Carro, Funcionario, Cliente, ContratoAluguel

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['placa', 'modelo', 'ano', 'foto', 'disponivel']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nomeFuncionario', 'emailFuncionario', 'cpfFuncionario', 'cargo', 'telefoneFuncionario']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nomeCliente', 'emailCliente', 'cpfCliente', 'telefoneCliente', 'enderecoCliente']

class ContratoAluguelForm(forms.ModelForm):
    class Meta:
        model = ContratoAluguel
        fields = ['carro', 'cliente', 'data_inicio', 'data_fim']