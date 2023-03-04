# Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. 
# Al parecer contiene el nombre de un alumno y la nota de un exámen. 
# ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
# Nombre Apellido ha sacado un Nota de nota.
# Ayuda:
# Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
# cadena = "zeréP nauJ,01"

# cadena a ordenar
cadena = input("Introduzca la frase a ordenar: ")

def ordenar_cadena(cadena):
    frase_a_ordenar = cadena[::-1]
    separar_frase = frase_a_ordenar.split(",")
    parte1 = separar_frase[1]
    parte2 = separar_frase[0]
    return "{} ha sacado un {} de nota.".format(parte1, parte2)

print(ordenar_cadena(cadena))