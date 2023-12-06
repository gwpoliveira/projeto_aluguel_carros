from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Carro(models.Model):
    placa=models.CharField('Placa:', max_length=8, unique=True)
    modelo = models.CharField('Modelo:', max_length=100)
    ano =  models.CharField('Modelo:', max_length=10)
    foto = models.ImageField('Foto:',upload_to='carros', blank=True, null=True)  
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
       return f"{self.modelo} - {self.placa}" - {self.ano}

class Funcionario(models.Model):
    nomeFuncionario = models.CharField('Nome:', max_length=254)
    emailFuncionario = models.EmailField('Email:')
    cpfFuncionario = models.CharField('CPF:',max_length=11)
    cargo = models.CharField('Cargo:',max_length=100)
    telefoneFuncionario = models.CharField(max_length=20, blank=True, null=True)
    
    
    def __str__(self):
       return f"{self.nomeFuncionario} - {self.cargo}"

class Cliente(models.Model):
    nomeCliente = models.CharField('Nome:', max_length=254)
    emailCliente = models.EmailField('Email:')
    cpfCliente = models.CharField('CPF:',max_length=11)
    telefoneCliente = models.CharField(max_length=20, blank=True, null=True)
    enderecoCliente = models.TextField('Endereço:')
    user = models.OneToOneField( get_user_model(),verbose_name="Usuário:", on_delete=models.CASCADE, unique=True ,blank=True, null=True)
    
    def __str__(self):
       return f"{self.nomeFuncionario} - {self.emailFuncionario}"

class ContratoAluguel(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    
    def __str__(self):
       return f"{self.id} - {self.carro.modelo} - {self.cliente.nomeCliente} - {self.data_inicio} - {self.data_fim}"

    
    

