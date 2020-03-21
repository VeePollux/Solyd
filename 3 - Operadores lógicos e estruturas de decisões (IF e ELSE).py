var_verdade = True
var_falso = False
print(var_falso)
print(type(var_falso), type(var_verdade))

if var_verdade == True:
    print("var verdade é verdadeiro")

'''
Comparar - ==
Diferente - !=
Maior igual - >=
Menor igual - <=
Maior - >
Menor - <
'''

a= "Alucard"
b= "Elias"
z = 50
x = 20

if z > x and a != b:
    print("Deu certo o if")
else:
    print("Não deu certo o if")


print("Opções:\n1 = Escreve Elias\n2 = Escreve Alucard\n3 = Escreve Goblin")
opcao = input("Escolha uma opção:")

if opcao == "1":
    print("Elias lindo")
elif opcao == "2": #se não ser = elif = else if
    print("Alucard gostoso")
elif opcao == "3":
    print("Goblin fofuxo")
else:
    print("Escolhe certo vagabunda")


idade = 16
if idade == 16:
    print("Você tem 16 anos")
else:
    print("Você não tem 16 anos")

comprimento = 13
if not comprimento == 13:
    print("Não tem 13 metros")
else:
    print("Tem 13 metros")