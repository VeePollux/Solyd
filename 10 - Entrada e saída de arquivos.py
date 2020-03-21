arquivo = open("arquivo.txt", "r+")
"""
w - write / escrever
r - read / ler
r+ - escrever e ler
a - append / adicionar coisas
b - binario
rb - para ler binario
"""
type(print(arquivo))
print(type(arquivo))
arquivo.write("Churrasqueira a controle remoto\nAperta o um e liga")

for x in range(0, 21):
    arquivo.write("\n" + str(x))

"""
Para ler depois tem q mudar lá em cima do arquivo, botando "r"
e n tendo esse resto pra cima pois ele n tem como escrever enquanto está para ler.
Mas se tiver em "r+" poderá ler e escrever.
"""

print(arquivo.read())

file = open("danzig father.jpg", "rb")
print(file.read())