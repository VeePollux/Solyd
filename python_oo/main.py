from veiculo import Veiculo

moto = Veiculo(2,"Yamaha", "Preto", 10)

print(moto)
print(type(moto))
print(moto.cor)
print(moto.tanque)
moto.abastecer(10)
print(moto.tanque)