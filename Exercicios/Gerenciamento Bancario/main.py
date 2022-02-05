'''Exercício: crie um software de gerenciamento bancario
Esse software será capaz de criar clientes e contas
Cada cliente possui nome, cpf e idade
Cada conta possui cliente, saldo, limite, sacar, depositar e consultar saldo
'''
from cliente import Cliente
from conta import Conta

Rosa = Cliente("Rosa", 455585, 55)
RosaC = Conta(Rosa, 100, 500)

print(RosaC.consulta())
RosaC.sacar(150)
print(RosaC.consulta())
RosaC.depositar(400)
print(RosaC.consulta())
RosaC.depositar(10)
print(RosaC.consulta())