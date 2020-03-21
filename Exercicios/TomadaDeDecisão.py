'''
5) Faça um algoritmo que peça a idade do usuário e a idade da sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve.
6) Faça um algoritmo que imprima 50 vezes o caractere "-" na tela (sem a utilização de laços de repetição).
8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.
9) Faça um algoritmo que verifica se um determinado valor é um número inteiro.
10) Faça um algoritmo que verifica se um determinado valor é uma String.
15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.
18) Faça um algoritmo que valide uma data. A mesma deve ser formada por dia, mês e ano.
Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida.
Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.'''

print("Questão 05\n")
vc=int(input("Digite sua idade: "))
mae=int(input("Digite a idade de sua mãe: "))
print("Sua mãe o teve com", (mae-vc), "anos")

print("Questão 06\n")
char="-"
print(50*char)
print("\n")

print("Questão 08\n")
a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
if(a>=b):
    print(a)
    print(b)
else:
    print(b)
    print(a)

print("Questão 09\n")
valor=float(input("Digite um valor: "))
if(valor//1==valor):#operador de divisão inteira(//), divide o valor inserido por 1, não altera seu valor mas remove sua parte decimal
    print("Seu valor é um número inteiro")
else:
    print("Seu valor não é um número inteiro")

print("Questão 10\n")
a=input("Digite um valor: ")
if(type(a)==str):
    print("Seu valor foi armazenado como String")
else:
    print("Não vai ter else. Seu valor sempre será uma string")

print("Questão 15\n")
print("Esse algoritmo irá descobrir se você digita uma vogal! \n")
letra=str(input("Digite um caractere: "))
if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"): #vogais minúsculas
    print("Seu caractere é uma vogal")
elif(letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U"): #vogais maiúsculas
    print("Seu caractere é uma vogal")

#foi necessário recorrer à documentação do python
print("Questão 18\n")
data=input("Digite uma data no formato DD/MM/AAAA: ")
#A função len conta quantos caracteres há numa string
if len(data) != 10: # qualquer string que tenha mais ou menos que 10 caracteres (formato padrão) será inválida
    print("FORMATO INVÁLIDO!")
else:
    print("SUA DATA FOI VALIDADA!!!")
print("\n")
