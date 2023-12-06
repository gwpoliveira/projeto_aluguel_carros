from django.contrib import admin
from .models import Carro, Funcionario, Cliente, ContratoAluguel

class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'ano', 'disponivel')
    search_fields = ('placa', 'modelo', 'ano')
    list_filter = ('disponivel',)

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nomeFuncionario', 'emailFuncionario', 'cpfFuncionario', 'cargo')
    search_fields = ('nomeFuncionario', 'emailFuncionario', 'cpfFuncionario', 'cargo')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nomeCliente', 'emailCliente', 'cpfCliente', 'telefoneCliente', 'enderecoCliente')
    search_fields = ('nomeCliente', 'emailCliente', 'cpfCliente')
    list_filter = ('user',)

class ContratoAluguelAdmin(admin.ModelAdmin):
    list_display = ('carro', 'cliente', 'data_inicio', 'data_fim')
    search_fields = ('carro__placa', 'cliente__nomeCliente')
    list_filter = ('data_inicio', 'data_fim')

admin.site.register(Carro, CarroAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(ContratoAluguel, ContratoAluguelAdmin)
