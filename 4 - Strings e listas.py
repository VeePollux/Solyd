frase = "Oi, tudo bem?"
lista_nomes = ["Seras Victoria", "Yako", "Nanami", "Chise"]
print(type(lista_nomes))
print(type(frase))

print(frase[0])
print(frase[5])
print(frase[0:12])
print(frase[0:13]) #sempre tem q
print(frase[0:13:3])
print(lista_nomes[-1])
print(lista_nomes[::-1])
print(frase[::-1])

lista_names = ["Maria", "João", "Jubileu"]
lista_names.append("Ricardão") #append sempre adiciona a palavra no final da lista
lista_names.append("Inácio")
lista_names.remove("João")
lista_names.insert(1 ,"Mika") #Inserir um nome em um determinado lugar
lista_names[2] = "Tecnosvaldo" #substituir um nome da lista
print(lista_names)
contador_maria = lista_names.count("Maria")
print(contador_maria)

listao = ["Chloe", "Lucifer", "Trixie"]
listao.clear()
print(listao)

print(len(frase)) #quantas letras tem
print(len(lista_names)) #quantas palavras tem

lista_dnv = ["Marcia", "Antonio", "Cleosvaldo", "Inacio"]
print(lista_dnv.pop()) #tira o ultimo nome da lista e mostra
print(lista_dnv.pop())
print(lista_dnv)

print(frase.lower()) #deixa tudo minusculo
print(frase) #N deixa minusculo permanentemente

frase_separada = frase.split(",") #separa a frase e transforma em uma lista
print(frase_separada)
print(type(frase_separada))
print(frase_separada[1])

frase_nova = frase + " Como vai você?"
print(frase_nova)

print(frase, "Como vai você?")