# views.py em aluguel_carros

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Carro, Funcionario, Cliente, ContratoAluguel
from .forms import CarroForm, FuncionarioForm, ClienteForm, ContratoAluguelForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
class ListarCarrosView(View):
    template_name = 'carro/listar_carros.html'

    def get(self, request, *args, **kwargs):
        carros = Carro.objects.all()
        return render(request, self.template_name, {'carros': carros})

class DetalhesCarroView(View):
    template_name = 'carro/detalhes_carro.html'

    def get(self, request, carro_id, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=carro_id)
        return render(request, self.template_name, {'carro': carro})

class AdicionarCarroView(View):
    template_name = 'carro/adicionar_carro.html'

    def get(self, request, *args, **kwargs):
        form = CarroForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
        return render(request, self.template_name, {'form': form})

class EditarCarroView(View):
    template_name = 'carro/editar_carro.html'

    def get(self, request, carro_id, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=carro_id)
        form = CarroForm(instance=carro)
        return render(request, self.template_name, {'form': form, 'carro': carro})

    def post(self, request, carro_id, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=carro_id)
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('listar_carros')
        return render(request, self.template_name, {'form': form, 'carro': carro})

class ExcluirCarroView(View):
    template_name = 'carro/excluir_carro.html'

    def get(self, request, carro_id, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=carro_id)
        return render(request, self.template_name, {'carro': carro})

    def post(self, request, carro_id, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=carro_id)
        carro.delete()
        return redirect('listar_carros')

# ___________ Funcionario _________________

class ListarFuncionariosView(View):
    template_name = 'funcionario/listar_funcionarios.html'

    def get(self, request, *args, **kwargs):
        funcionarios = Funcionario.objects.all()
        return render(request, self.template_name, {'funcionarios': funcionarios})

class DetalhesFuncionarioView(View):
    template_name = 'funcionario/detalhes_funcionario.html'

    def get(self, request, funcionario_id, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        return render(request, self.template_name, {'funcionario': funcionario})

class AdicionarFuncionarioView(View):
    template_name = 'funcionario/adicionar_funcionario.html'

    def get(self, request, *args, **kwargs):
        form = FuncionarioForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
        return render(request, self.template_name, {'form': form})

class EditarFuncionarioView(View):
    template_name = 'funcionario/editar_funcionario.html'

    def get(self, request, funcionario_id, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        form = FuncionarioForm(instance=funcionario)
        return render(request, self.template_name, {'form': form, 'funcionario': funcionario})

    def post(self, request, funcionario_id, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('listar_funcionarios')
        return render(request, self.template_name, {'form': form, 'funcionario': funcionario})

class ExcluirFuncionarioView(View):
    template_name = 'funcionario/excluir_funcionario.html'

    def get(self, request, funcionario_id, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        return render(request, self.template_name, {'funcionario': funcionario})

    def post(self, request, funcionario_id, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=funcionario_id)
        funcionario.delete()
        return redirect('listar_funcionarios')

# ___________ Cliente _________________

class ListarClientesView(View):
    template_name = 'cliente/listar_clientes.html'

    def get(self, request, *args, **kwargs):
        clientes = Cliente.objects.all()
        return render(request, self.template_name, {'clientes': clientes})

class DetalhesClienteView(View):
    template_name = 'cliente/detalhes_cliente.html'

    def get(self, request, cliente_id, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        return render(request, self.template_name, {'cliente': cliente})

class AdicionarClienteView(View):
    template_name = 'cliente/adicionar_cliente.html'

    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
        return render(request, self.template_name, {'form': form})

class EditarClienteView(View):
    template_name = 'cliente/editar_cliente.html'

    def get(self, request, cliente_id, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = ClienteForm(instance=cliente)
        return render(request, self.template_name, {'form': form, 'cliente': cliente})

    def post(self, request, cliente_id, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
        return render(request, self.template_name, {'form': form, 'cliente': cliente})

class ExcluirClienteView(View):
    template_name = 'cliente/excluir_cliente.html'

    def get(self, request, cliente_id, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        return render(request, self.template_name, {'cliente': cliente})

    def post(self, request, cliente_id, *args, **kwargs):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        cliente.delete()
        return redirect('listar_clientes')
    
# ___________ Contrato Aluguel _________________

class ListarContratosAluguelView(View):
    template_name = 'contrato_aluguel/listar_contratos_aluguel.html'

    def get(self, request, *args, **kwargs):
        contratos_aluguel = ContratoAluguel.objects.all()
        return render(request, self.template_name, {'contratos_aluguel': contratos_aluguel})

class DetalhesContratoAluguelView(View):
    template_name = 'contrato_aluguel/detalhes_contrato_aluguel.html'

    def get(self, request, contrato_id, *args, **kwargs):
        contrato_aluguel = get_object_or_404(ContratoAluguel, pk=contrato_id)
        return render(request, self.template_name, {'contrato_aluguel': contrato_aluguel})

class AdicionarContratoAluguelView(View):
    template_name = 'contrato_aluguel/adicionar_contrato_aluguel.html'

    def get(self, request, *args, **kwargs):
        form = ContratoAluguelForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContratoAluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos_aluguel')
        return render(request, self.template_name, {'form': form})

class EditarContratoAluguelView(View):
    template_name = 'contrato_aluguel/editar_contrato_aluguel.html'

    def get(self, request, contrato_id, *args, **kwargs):
        contrato_aluguel = get_object_or_404(ContratoAluguel, pk=contrato_id)
        form = ContratoAluguelForm(instance=contrato_aluguel)
        return render(request, self.template_name, {'form': form, 'contrato_aluguel': contrato_aluguel})

    def post(self, request, contrato_id, *args, **kwargs):
        contrato_aluguel = get_object_or_404(ContratoAluguel, pk=contrato_id)
        form = ContratoAluguelForm(request.POST, instance=contrato_aluguel)
        if form.is_valid():
            form.save()
            return redirect('listar_contratos_aluguel')
        return render(request, self.template_name, {'form': form, 'contrato_aluguel': contrato_aluguel})

class ExcluirContratoAluguelView(View):
    template_name = 'contrato_aluguel/excluir_contrato_aluguel.html'

    def get(self, request, contrato_id, *args, **kwargs):
        contrato_aluguel = get_object_or_404(ContratoAluguel, pk=contrato_id)
        return render(request, self.template_name, {'contrato_aluguel': contrato_aluguel})

    def post(self, request, contrato_id, *args, **kwargs):
        contrato_aluguel = get_object_or_404(ContratoAluguel, pk=contrato_id)
        contrato_aluguel.delete()
        return redirect('listar_contratos_aluguel')