# views.py em aluguel_carros
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import DevolucaoForm
from .models import Carro, Funcionario, Cliente, ContratoAluguel
from .forms import CarroForm, FuncionarioForm, ClienteForm, ContratoAluguelForm, DevolucaoCarroForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

class CustomLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')  # Substitua 'home' pelo nome da sua URL de página inicial
    
class HomeView(TemplateView):
    template_name = 'home.html'  
    
    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['carros'] = Carro.objects.all()[:10]
      return context

class ListarCarrosView(ListView):
    model = Carro
    template_name = 'carro/listar_carros.html'
    context_object_name = 'carros'
    ordering = 'modelo'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(modelo__icontains=pesquisa)  # Corrigido para 'modelo'

        return queryset

class DetalhesCarroView(DetailView):
    model = Carro
    template_name = 'carro/detalhes_carro.html'
    context_object_name = 'carro'
    # pk_url_kwarg = 'id'
    
class AdicionarCarroView(LoginRequiredMixin,CreateView):
    model = Carro
    template_name = 'carro/adicionar_carro.html'
    form_class = CarroForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro cadastrado com sucesso!")
        return reverse_lazy('listar_carros')

class EditarCarroView(LoginRequiredMixin,UpdateView):
    model = Carro
    template_name = 'carro/editar_carro.html'
    form_class = CarroForm    
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro atualizado com sucesso!")
        return reverse('listar_carros')

class ExcluirCarroView(LoginRequiredMixin,DeleteView):
    model = Carro
    template_name = 'carro/carro_confirm_delete.html'
    # pk_url_kwarg = 'id'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Carro deletado com sucesso!")
        return reverse('listar_carros')

# ___________ Funcionario _________________

class ListarFuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionario/listar_funcionarios.html'
    context_object_name = 'funcionarios'
    ordering = 'nomeFuncionario'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(nome__icontains=pesquisa)

        return queryset

class DetalhesFuncionarioView(DetailView):
    model = Funcionario
    template_name = 'funcionario/detalhes_funcionario.html'
    context_object_name = 'funcionario'

class AdicionarFuncionarioView(LoginRequiredMixin,CreateView):
    model = Funcionario
    template_name = 'funcionario/adicionar_funcionario.html'
    form_class = FuncionarioForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Funcionário cadastrado com sucesso!")
        return reverse('listar_funcionarios')

class EditarFuncionarioView(LoginRequiredMixin,UpdateView):
    model = Funcionario
    template_name = 'funcionario/editar_funcionario.html'
    form_class = FuncionarioForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Funcionário atualizado com sucesso!")
        return reverse('listar_funcionarios')

class ExcluirFuncionarioView(LoginRequiredMixin,DeleteView):
    model = Funcionario
    template_name = 'funcionario/funcionario_confirm_delete.html'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Funcionário deletado com sucesso!")
        return reverse('listar_funcionarios')

# ___________ Cliente _________________

class ListarClientesView(ListView):
    model = Cliente
    template_name = 'cliente/listar_clientes.html'
    context_object_name = 'clientes'
    ordering = 'nomeCliente'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(nome__icontains=pesquisa)

        return queryset

class DetalhesClienteView(DetailView):
    model = Cliente
    template_name = 'cliente/detalhes_cliente.html'
    context_object_name = 'cliente'

class AdicionarClienteView(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = 'cliente/adicionar_cliente.html'
    form_class = ClienteForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cliente cadastrado com sucesso!")
        return reverse('listar_clientes')

class EditarClienteView(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = 'cliente/editar_cliente.html'
    form_class = ClienteForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cliente atualizado com sucesso!")
        return reverse('listar_clientes')

class ExcluirClienteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = 'cliente/cliente_confirm_delete.html'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Cliente deletado com sucesso!")
        return reverse('listar_clientes')
    
# ___________ Contrato Aluguel _________________

class ListarContratosView(LoginRequiredMixin,ListView):
    model = ContratoAluguel
    template_name = 'contrato/listar_contratos.html'
    context_object_name = 'contratos'
    ordering = 'data_inicio'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        pesquisa = self.request.GET.get('pesquisa')

        # Se o botão de limpar pesquisa foi clicado, ignore o parâmetro de pesquisa
        if 'limpar_pesquisa' in self.request.GET:
            pesquisa = ''

        if pesquisa:
            queryset = queryset.filter(cliente__nome__icontains=pesquisa)

        return queryset

# class DetalhesContratoView(LoginRequiredMixin,DetailView):
#     model = ContratoAluguel
#     template_name = 'contrato/detalhes_contrato.html'
#     context_object_name = 'contrato'

class DetalhesContratoView(LoginRequiredMixin, DetailView):
    model = ContratoAluguel
    template_name = 'contrato/detalhes_contrato.html'
    context_object_name = 'contrato'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contrato = self.get_object()
        context['contrato'] = contrato
        return context



class AdicionarContratoView(LoginRequiredMixin,CreateView):
    model = ContratoAluguel
    template_name = 'contrato/adicionar_contrato.html'
    form_class = ContratoAluguelForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contrato de aluguel cadastrado com sucesso!")
        return reverse('listar_contratos')

    def form_valid(self, form):
        # Obtenha o carro associado ao contrato
        carro_id = form.cleaned_data['carro'].id
        carro = get_object_or_404(Carro, pk=carro_id)

        if carro.esta_disponivel():
            # Se o carro estiver disponível, prossiga com a criação do contrato
            messages.add_message(self.request, messages.SUCCESS, "Contrato de aluguel cadastrado com sucesso!")
            response = super().form_valid(form)

            # Atualize o status do carro para indisponível
            carro.disponivel = False
            carro.save()

            return response

        # Lógica caso o carro não esteja disponível
        messages.add_message(self.request, messages.ERROR, "O carro selecionado não está disponível.")
        return redirect('listar_carros')  # Redirecione para a lista de carros ou ajuste conforme necessário

class EditarContratoView(LoginRequiredMixin,UpdateView):
    model = ContratoAluguel
    template_name = 'contrato/editar_contrato.html'
    form_class = ContratoAluguelForm
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contrato de aluguel atualizado com sucesso!")
        return reverse('listar_contratos')

class ExcluirContratoView(LoginRequiredMixin,DeleteView):
    model = ContratoAluguel
    template_name = 'contrato/contrato_confirm_delete.html'
    
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, "Contrato de aluguel deletado com sucesso!")
        return reverse('listar_contratos')

class DevolverContratoView(DetailView):
    model = ContratoAluguel
    template_name = 'contrato/devolver_contrato.html'  # substitua pelo seu template

    def get(self, request, *args, **kwargs):
        contrato = self.get_object()

        if contrato.devolvido:
            messages.add_message(request, messages.WARNING, "Este contrato já foi devolvido.")
            return redirect('listar_contratos')

        # Atualize o status do contrato para devolvido
        contrato.devolvido = True
        contrato.save()

        # Atualize o status do carro para disponível
        contrato.carro.disponivel = True
        contrato.carro.save()

        messages.add_message(request, messages.SUCCESS, "Contrato de aluguel devolvido com sucesso!")
        return redirect('listar_contratos')