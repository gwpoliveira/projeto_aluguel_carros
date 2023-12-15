# aluguel_carros/urls.py

from django.urls import path
from .views import (
    ListarCarrosView, DetalhesCarroView, AdicionarCarroView,
    EditarCarroView, ExcluirCarroView, ListarFuncionariosView,
    DetalhesFuncionarioView, AdicionarFuncionarioView, EditarFuncionarioView,
    ExcluirFuncionarioView, ListarClientesView, DetalhesClienteView,
    AdicionarClienteView, EditarClienteView, ExcluirClienteView, HomeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('listar_carros/', ListarCarrosView.as_view(), name='listar_carros'),
    path('carro/<int:carro_id>/', DetalhesCarroView.as_view(), name='detalhes_carro'),
    path('adicionar_carro/', AdicionarCarroView.as_view(), name='adicionar_carro'),
    path('editar_carro/<int:carro_id>/', EditarCarroView.as_view(), name='editar_carro'),
    path('excluir_carro/<int:carro_id>/', ExcluirCarroView.as_view(), name='excluir_carro'),

    path('listar_funcionarios/', ListarFuncionariosView.as_view(), name='listar_funcionarios'),
    path('funcionario/<int:funcionario_id>/', DetalhesFuncionarioView.as_view(), name='detalhes_funcionario'),
    path('adicionar_funcionario/', AdicionarFuncionarioView.as_view(), name='adicionar_funcionario'),
    path('editar_funcionario/<int:funcionario_id>/', EditarFuncionarioView.as_view(), name='editar_funcionario'),
    path('excluir_funcionario/<int:funcionario_id>/', ExcluirFuncionarioView.as_view(), name='excluir_funcionario'),

    path('listar_clientes/', ListarClientesView.as_view(), name='listar_clientes'),
    path('cliente/<int:cliente_id>/', DetalhesClienteView.as_view(), name='detalhes_cliente'),
    path('adicionar_cliente/', AdicionarClienteView.as_view(), name='adicionar_cliente'),
    path('editar_cliente/<int:cliente_id>/', EditarClienteView.as_view(), name='editar_cliente'),
    path('excluir_cliente/<int:cliente_id>/', ExcluirClienteView.as_view(), name='excluir_cliente'),
]
