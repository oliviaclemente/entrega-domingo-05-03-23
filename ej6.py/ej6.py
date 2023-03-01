def separar(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    
    return pares, impares

pares, impares = separar([6, 5, 2, 1, 7])
print(pares)
print(impares)
