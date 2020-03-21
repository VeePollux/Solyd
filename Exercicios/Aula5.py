print("Não sei que nome botar pro programa")
print("#####################################")

numero_de_convidados = input("Digite o numero de convidados:")
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_de_convidados=(input("Digite o nome do convidado #" + str(i) + ":"))
    i += 1
    lista_de_convidados.append(nome_de_convidados)

for nome in lista_de_convidados:
    print(nome)

