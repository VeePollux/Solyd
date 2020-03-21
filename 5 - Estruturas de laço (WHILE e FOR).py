animes = ["Mahou Tsukai", "Hellsing", "Shin Sekai", "Kuroshitsuji"]
for anime in animes:
    print(anime)

numeros= range(8)
for n in numeros:
    print(n)
lista_numeros= range(5,8)
for ln in lista_numeros:
    print(ln)

list_numbers= range(1,20,5)
for ln in list_numbers:
    print(ln)
'''
Pode ser usado apenas o range, tipo, "for item in range(~~)"
obviamente quando n tem mais de um range
'''
for item in range (4): #se for para fazer palavras é mais fácil usar o "for item in (alguma coisa)
    print(animes[item]) #pois se tiver menos palavras na lista do que tem no range irá dar erro

for i in range(len(animes)):
    print(animes[i])

palavra= "Churrasqueira elétrica"
for letra in palavra:
    print(letra)

i=0
while i<10: #Enquanto o while for true ele irá rodar, se for false nem irá entrar nele
    print("i ainda é maior que 10:", i)
    i = i+1  #não se esquecer de botar valores aqui, se não viraria um loop infinito
print("Acabou o while:", i)

x=0
x=x+10
x=x+10
print(x)

contador = 0
lista_frutas = ["Melão", "Melancia", "Banana", "Maçã", "Abacaxi"]
for fruta in lista_frutas:
    contador += 1
print(contador) #O mais facil ainda é usando o len
print(len(lista_frutas))

numero = 0
while True: #numero infinito
    print(numero)
    if numero == 10: #numero n é igual a vinte então n passou aqui
        break
    numero +=1 #foi somando 1 até chegar a dez, quando chegar a dez ele irá quebrar
print("Saiu do While")