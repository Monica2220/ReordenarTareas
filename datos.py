
#datos.py


# Lista donde se guardan todas las tareas.

tareas = []


def obtener_tareas():
    return tareas


def guardar_tarea(tarea):
    tareas.append(tarea)


def eliminar_tarea_por_indice(indice):
    return tareas.pop(indice)
