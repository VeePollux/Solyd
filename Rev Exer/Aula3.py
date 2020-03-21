print("Você está apto a entrar no exército? Faça este teste e descubra agora mesmo!!!!")
print("###############################################################################")
idade = input("Escreva sua idade:")
altura = input("Escreva sua altura(em metros):")
peso = input("Escreva seu peso(em Kg):")

if idade >= str(18) and altura >= float(1.70) and peso >= float(60):
    print("Está apto a entrar")
else:
    print("Não está apto")