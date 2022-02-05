from cliente import Cliente
class Conta:

    def __init__(self, cliente, saldo, limite):
        Cliente.__init__(self, cliente.nome, cliente.cpf, cliente.idade)
        self.saldo = saldo
        self.limite = limite
    
    def sacar (self, valorS):
        if(valorS > self.saldo):
            print("Saldo insuficiente.")
        else:
            self.saldo -= valorS

    def depositar (self, valorD):
        if((self.limite)<(self.saldo + valorD)):
            print("Limite atingido.")
        else:
            self.saldo += valorD
 
    def consulta (self):
        return self.saldo