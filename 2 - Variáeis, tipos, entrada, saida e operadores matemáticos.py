print("Hello world")
print("Hello!I'm a text")
print("Mahou tsukai no yome\nMelhor anime")
print("Ikemen Sengoku!\tNobunaga Rocks")

nome = "Vanessa"
idade = 16
altura = 1.66
tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)
print(nome)
print(idade)
print(altura)
print(tipo_nome)
print(tipo_idade)
print(tipo_altura)

print(nome, "tem", idade, "anos e", altura, "de altura")
print(nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura")

frase = nome, "tem", idade, "anos e", altura, "de altura"
print(frase)
frase_dois = nome + " tem " + str(idade) + " anos e " + str(altura) + " de altura"
print(frase_dois)

numero1 = 10
numero2 = 145
numero3 = 5.1
resultado = numero2 - numero1 / numero3 * 3
print(resultado)

elevado_ao_quadrado = 10 ** 2
print(elevado_ao_quadrado)

raiz_quadrada = 4 ** (1/2) #comentário que não aparece no código, é usado para colocar algo que se foi feito para saber
print(raiz_quadrada)  #tipo, aqui foi usada a raiz quadrada

'''
Aqui é para poder deixar um texto como um
comentário também
'''

name = input("Escreva seu nome:")
age = input("Escreva sua idade poura:")
height = input("Escreva sua altura caralho:")
print(name, "tem", age, "anos e", height, "de altura")
print(type(name), type(age), type(height))
