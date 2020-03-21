

def maior (argumento):
    maior_item = argumento [0]
    for item in argumento:
        if item > maior_item:
            maior_item = item
    return maior_item
print(maior([888,65,98,258]))




def menor (argumento):
    menor_item = argumento [0]
    for item in argumento:
        if item < menor_item:
            menor_item = item
    return menor_item
print(menor([155,558,87,1]))
