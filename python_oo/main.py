from carro import Carro
from veiculo import Veiculo

caminhaoP = Veiculo(2,"Yamaha", "Preto", 10)
carroV = Carro("Vermelho", 4, "bmw", 30)

print(caminhaoP)
print(type(caminhaoP))
print(caminhaoP.cor)
print(caminhaoP.tanque)
caminhaoP.abastecer(500)
print(caminhaoP.tanque)

print(carroV.cor)
print(carroV.tanque)
carroV.abastecer(30)
print(carroV.tanque)
carroV.abastecer(10)
print(carroV.tanque)