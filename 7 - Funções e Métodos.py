def soma (numero1, numero2):
    resp = numero1 + numero1
    return resp
retorno = soma(12.65, 28.3)
print(retorno)

def imprime_oi():
    print("Oi")
imprime_oi()
imprime_oi()

def tem_sete_itens (argumento):
    if len(argumento) == 7:
        return True
    else:
        return False
print(tem_sete_itens("1234567"))
if tem_sete_itens("1234567"):
    print("tem sete")