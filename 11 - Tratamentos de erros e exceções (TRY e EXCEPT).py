try:
    a = 10/0
except:
    print("Erro: Divisão por zero n se faz")
print("aaaaaa")

try:
    variavel_aleatoria
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except NameError:
    print("Erro: Digitação errada")

import time
def abre_arquivo():
    try:
        open("arquivo_que_nao_existia.txt")
        return True
    except Exception as erro:
        print("Aconteceu algum erro:", erro)
        return False
while not abre_arquivo():
    print("Tentanto abrir o arquivo")
    time.sleep(5)
print("Consegui abrir o arquivo")
"""
No momento que foi criado o arquivo ele consegue abrir, mas enquanto n existir
ele "return False" e vai para o "While not", virando um ciclo.
"""