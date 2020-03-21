minha_lista = ["Seth", "Kratos"]  #A lista é dinâmica, tem índices e etc
minha_tupla = ("Seth", "Kratos")  #Tuple sempre terá os mesmo elementos, mas tem indice, podendo pegar os itens
meu_dicionario = {"nome" : "Elias", "idade" : "500"} #dict n está ordenado
meu_conjunto = {"Seth", "Kratos"} #set o conjunto não é ordenado, n tem ordem, ou sejan n tem indice, mas pd adc coisas

if "Seth" in minha_lista:
    print("Seth está na coleção")

print(meu_dicionario["idade"])
print(len(meu_dicionario)) #len pode ser usado em qualquer coleção, é usado para saber o tamanho

if "Elias" in meu_dicionario.values(): #podemos procurar no dict
    print("Elias está no dicionario")

for valores in meu_dicionario.values(): #values veem os "valores" do dict
    print(valores)
for valores in meu_dicionario.keys(): #keys veem as "chaves" do dict
    print(valores)
meu_dicionario["idade"] = 1000 #Pode ser mudado os valores dentro de um dict
print(meu_dicionario)

meu_dicionario["endereço"] = "Av. João das Neves" #No dict pode ser adicionado novos elementos
print(meu_dicionario)
'''
No dict podemos usar clear (para limpar tudo), pop (para remover algo), uptade (para modificar o valor,
mas ja fizemos de outra maneira
'''

meu_conjunto.add("Ikuto") #pode adicionar novos elementos
meu_conjunto.add("Kratos") #elementos iguais aparecem uma só vez, quando n queremos dados repetidos
print(meu_conjunto)

if "Seth" in meu_conjunto:
    print("Está no conjunto")
'''
Fazer pelo conjunto ou dict o if em vez da lista, por exemplo, faz com q o programa n precise percorrer a ordem
já que no conjunto não existem ordens, então teremos uma resposta mais rápida do q fazendo pela lista
'''

meu_conjunto.remove("Kratos")
print(meu_conjunto)
'''
lista = []
tupla = ()
dicionario = dict {}
conjunto = {}
'''
loucura = [(1,3),({"Elias": "Gostoso"},{"Masamune","Uruha"})]#Lista com duas tuplas, uma com um dict e um set
print(loucura)