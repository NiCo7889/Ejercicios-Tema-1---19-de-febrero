# Crea un script llamado descomposicion.py que realice las siguientes tareas:
# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que 
# por ejemplo si se introduce el número 3647:
# python descomposicion.py 3647
# El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas 
# de formateo:
# 0007
# 0040
# 0600
# 3000
# Pista
# Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. 
# Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas,
# números y viceversa


def Descomposicion(num):
    numero = str(num)
    numero = list(numero)
    numero = numero[::-1]
    n = len(numero) - 1
    # Por ultimo recorremos esta lista para imprimir: tantos 0 a la izq como (n - i), letra, y tantos a la dcha como i
    for i, letra in enumerate(numero):
        print("{}{}{}".format((n - i)*"0", letra, i*"0")) 
    return num

print(Descomposicion(8975))