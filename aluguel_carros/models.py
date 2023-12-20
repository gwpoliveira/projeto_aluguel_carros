from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Carro(models.Model):
    placa=models.CharField('Placa:', max_length=8, unique=True)
    modelo = models.CharField('Modelo:', max_length=100)
    ano =  models.CharField('Ano:', max_length=10)
    foto = models.ImageField('Foto:', upload_to='carros', blank=True, null=True)  
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.modelo} - {self.placa} - {self.ano} - {self.disponivel}"
   
    def esta_disponivel(self):
        return self.disponivel   

class Funcionario(models.Model):
    nomeFuncionario = models.CharField('Nome:', max_length=254)
    emailFuncionario = models.EmailField('Email:')
    cpfFuncionario = models.CharField('CPF:',max_length=11)
    cargo = models.CharField('Cargo:',max_length=100)
    telefoneFuncionario = models.CharField('Contato:',max_length=20, blank=True, null=True)
    
    
    def __str__(self):
       return f"{self.nomeFuncionario} - {self.cargo}"

class Cliente(models.Model):
    nomeCliente = models.CharField('Nome:', max_length=254)
    emailCliente = models.EmailField('Email:')
    cpfCliente = models.CharField('CPF:',max_length=11)
    telefoneCliente = models.CharField('Contato', max_length=20, blank=True, null=True)
    enderecoCliente = models.TextField('Endereço:')
    
    def __str__(self):
       return f"{self.nomeCliente} - {self.emailCliente}"

class ContratoAluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
       return f"{self.id} - {self.carro.modelo} - {self.cliente.nomeCliente} - {self.data_inicio} - {self.data_fim}"

class DevolucaoCarro(models.Model):
    contrato = models.OneToOneField('ContratoAluguel', on_delete=models.CASCADE)
    data_devolucao = models.DateField('Data de Devolução')
    descricao_avaria = models.TextField('Descrição da Avaria', blank=True, null=True)  
    def __str__(self):
        return f"Devolução para Contrato {self.contrato.id} em {self.data_devolucao}"
    

