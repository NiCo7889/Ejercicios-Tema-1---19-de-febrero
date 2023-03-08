# Siempre que quiera hacer los test tengo que crear una carpeta "test" en la que haya dos archivos. Uno es de los "test" y otro "__init__.py".
# "__init__.py" no tiene que tener nada, solo tiene que estar, porque es un archivo que sirve para dar forma de paquete a la carpeta.
# Si quiero crear mi propio paquete tengo que tener una carpeta __init__.py
"""
Un módulo es un archivo de Python cuyos objetos (funciones, clases, excepciones, etc.) pueden ser accedidos desde otro archivo. Se trata simplemente de una forma de organizar 
grandes códigos. Un paquete es una carpeta que contiene varios módulos. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.
Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta.Python tiene sus propios 
módulos, los cuales forman parte de su librería de módulos estándar, que también pueden ser importados.
PEP 8: importación
La importación de módulos debe realizarse al comienzo del documento, en orden alfabético de paquetes y módulos.Primero deben importarse los módulos propios de Python.
Luego, los módulos de terceros y finalmente, los módulos propios de la aplicación. Entre cada bloque de imports, debe dejarse una línea en blanco.
"""
import unittest
import Ejercicio1 as ej1
import Ejercicio2 as ej2
import Ejercicio3 as ej3
import Ejercicio4 as ej4
import descomposicion as ej5
import Ejercicio6 as ej6
import Ejercicio7 as ej7


class TestEjercicios(unittest.TestCase):

    def test_ordenar_cadena(self):
        self.assertEqual(ej1.ordenar_cadena("zeréP nauJ,01"), "Juan Pérez ha sacado un 10 de nota.")

    def test_numero_magico_excepcion(self):
        self.assertRaises(ValueError, ej2.numero_valido, "807")

    def test_numero_valido(self):
        self.assertEqual(ej2.num("7"), "Resultado: 777777777")

    def test_ele_repetidos(self):
        self.assertEqual(ej3.ele_repetidos(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a']), ['h', 'o', 'l', 'a', ' ', 'u', 'n'])

    def test_(self):
        self.assertEqual(ej4.crear_cola_tareas([("4", 'Realizar análisis de requisitos'), ("3", 'Diseñar la base de datos'), ("1", 'Desarrollar la funcionalidad principal'), ("2", 'Realizar pruebas unitarias')]), (['Desarrollar la funcionalidad principal', 'Realizar pruebas unitarias', 'Diseñar la base de datos', 'Realizar análisis de requisitos']))

    def test_(self):
        self.assertEqual(ej5.Descomposicion("8975"),["0005", "0070", "0900", "8000", "8975"])
    
    def test_separar(self):
        self.assertEqual(ej6.separar([6,5,2,1,7,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), ([2, 4, 6, 6, 8, 10, 12, 14, 16, 18, 20],[1, 3, 5, 5, 7, 7, 9, 11, 13, 15, 17, 19]))
    
    def test_(self):
        self.assertEqual(ej7.agregar_una_vez([1, 5, -2], "Hola"), [1, 5, -2, "Hola"])