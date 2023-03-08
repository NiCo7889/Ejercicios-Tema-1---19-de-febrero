"""
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) 
pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar 
grandes códigos.
Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, 
podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.
Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python 
entienda que se trata de un paquete y no de una simple carpeta.
Python tiene sus propios módulos, los cuales forman parte de su librería de módulos 
estándar, que también pueden ser importados.
PEP 8: importación
La importación de módulos debe realizarse al comienzo del documento, en orden alfabético 
de paquetes y módulos.
Primero deben importarse los módulos propios de Python. Luego, los módulos de terceros 
y finalmente, los módulos propios de la aplicación.
Entre cada bloque de imports, debe dejarse una línea en blanco.
"""
import os
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')