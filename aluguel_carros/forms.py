from django import forms
from .models import Carro, Funcionario, Cliente, ContratoAluguel, DevolucaoCarro


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
class DevolucaoCarroForm(forms.ModelForm):
    class Meta:
        model = DevolucaoCarro
        fields = ['contrato', 'data_devolucao', 'descricao_avaria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione opções adicionais ao campo 'contrato' se necessário
class DevolucaoForm(forms.Form):
    descricao_avaria = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

