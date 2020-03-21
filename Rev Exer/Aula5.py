numero_convidados = (input("Escreva o numero de convidados:"))
lista_convidados = []

i = 1
while i <= int(numero_convidados):
    nome_convidados = (input ("Escreva o nome do convidado #" + str(i) + ":")
    i += 1
    lista_convidados.append(nome_convidados)

for convidado in lista_convidados:
    print(convidado)

print("Teste1")
