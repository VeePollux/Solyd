class Veiculo:

    def __init__(self, rodas, marca, cor, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque


    def abastecer (self, litros):
        self.tanque += litros