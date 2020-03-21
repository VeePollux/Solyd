def maior (coleção):
    maior_item = coleção[0]
    for item in coleção:
        if item > maior_item:
            maior_item = item
    return maior_item

print(maior([1,2,8,15,258,565,216,69885]))

def menor (coleção):
    menor_item = coleção[0]
    for item in coleção:
        if menor_item > item:
            menor_item = item
    return menor_item

print(menor([1,98,62,544,548]))