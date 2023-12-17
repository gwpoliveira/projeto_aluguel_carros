# aluguel_carros/urls.py

from django.urls import path
from .views import (
    ListarCarrosView, DetalhesCarroView, AdicionarCarroView,
    EditarCarroView, ExcluirCarroView, ListarFuncionariosView,
    DetalhesFuncionarioView, AdicionarFuncionarioView, EditarFuncionarioView,
    ExcluirFuncionarioView, ListarClientesView, DetalhesClienteView,
    AdicionarClienteView, EditarClienteView, ExcluirClienteView,
)

urlpatterns = [
    path('listar_carros/', ListarCarrosView.as_view(), name='listar_carros'),
    path('carro/<int:pk>/', DetalhesCarroView.as_view(), name='detalhes_carro'),
    path('carro/adicionar_carro/', AdicionarCarroView.as_view(), name='adicionar_carro'),
    path('carro/editar_carro/<int:pk>/', EditarCarroView.as_view(), name='editar_carro'),
    path('carro/excluir_carro/<int:pk>/', ExcluirCarroView.as_view(), name='excluir_carro'),

    path('listar_funcionarios/', ListarFuncionariosView.as_view(), name='listar_funcionarios'),
    path('funcionario/<int:pk>/', DetalhesFuncionarioView.as_view(), name='detalhes_funcionario'),
    path('adicionar_funcionario/', AdicionarFuncionarioView.as_view(), name='adicionar_funcionario'),
    path('editar_funcionario/<int:pk>/', EditarFuncionarioView.as_view(), name='editar_funcionario'),
    path('excluir_funcionario/<int:pk>/', ExcluirFuncionarioView.as_view(), name='excluir_funcionario'),

    path('listar_clientes/', ListarClientesView.as_view(), name='listar_clientes'),
    path('cliente/<int:pk>/', DetalhesClienteView.as_view(), name='detalhes_cliente'),
    path('adicionar_cliente/', AdicionarClienteView.as_view(), name='adicionar_cliente'),
    path('editar_cliente/<int:pk>/', EditarClienteView.as_view(), name='editar_cliente'),
    path('excluir_cliente/<int:pk>/', ExcluirClienteView.as_view(), name='excluir_cliente'),
]
