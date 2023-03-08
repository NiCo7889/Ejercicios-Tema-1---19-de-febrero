# Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad 
# (cuanto menor es el número de orden, más prioridad).
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
# Sugerencia
# Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.


def crear_cola_tareas(tareas_prioridad):
    # Ordenar la lista de tareas según su prioridad
    tareas_prioridad.sort()
    # Crear una cola vacía para almacenar las tareas ordenadas
    cola_tareas = []
    # Agregar cada tarea a la cola en el orden correspondiente
    for tarea in tareas_prioridad:
        cola_tareas.append(tarea[1])
    # Retornar la cola de tareas ordenadas
    return cola_tareas

tareas_prioridad = [(4, 'Realizar análisis de requisitos'),
                    (3, 'Diseñar la base de datos'),
                    (1, 'Desarrollar la funcionalidad principal'),
                    (2, 'Realizar pruebas unitarias')]

cola_tareas_ordenadas = crear_cola_tareas(tareas_prioridad)

print(cola_tareas_ordenadas)