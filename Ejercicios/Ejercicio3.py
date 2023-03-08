# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento 
# en la nueva lista:
# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']


lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

def ele_repetidos(lista_1, lista_2):
    lista_3=[]
    for palabra in lista_1:
        if palabra in lista_2 and palabra not in lista_3:
            lista_3.append(palabra)
    return lista_3

print(ele_repetidos(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a']))