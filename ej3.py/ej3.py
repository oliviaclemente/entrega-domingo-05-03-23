lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def lista():
    lista_3=[]
    for item in lista_1:
        if item in lista_2 and item not in lista_3:
            lista_3.append(item)
    return lista_3

print(lista())
            