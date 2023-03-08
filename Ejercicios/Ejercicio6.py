# Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares.
# Por ejemplo:
# pares, impares = separar([6,5,2,1,7])
# print(pares)
# print(impares)
# [2, 6]
# [1, 5, 7]
# Sugerencia
# Para ordenar una lista automáticamente puedes utilizar el método .sort().


def separar(lista):
    if len(lista) == 0:
        return [], []
    else:
        pares, impares = separar(lista[1:])
        if lista[0] % 2 == 0:
            pares.append(lista[0])
            pares.sort()
        else:
            impares.append(lista[0])
            impares.sort()
        return pares, impares

pares, impares = separar([6,5,2,1,7,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("Lista de pares: {}, lista impares: {}.".format(pares, impares))