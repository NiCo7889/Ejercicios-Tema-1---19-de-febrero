# Siempre que quiera hacer los test tengo que crear una carpeta "test" en la que haya dos archivos. Uno es de los "test" y otro "__init__.py".
# "__init__.py" no tiene que tener nada, solo tiene que estar, porque es un archivo que sirve para dar forma de paquete a la carpeta.
# Si quiero crear mi propio paquete tengo que tener una carpeta __init__.py
import copy
import unittest
import Ejercicio1 as Ej1
import Ejercicio2 as Ej2
import Ejercicio3 as Ej3
import Ejercicio4 as Ej4
import Ejercicio5 as Ej5
import Ejercicio6 as Ej6
import Ejercicio7 as Ej7


class TestEjercicios(unittest.TestCase):
 
 

if __name__ == '__main__':
 unittest.main()