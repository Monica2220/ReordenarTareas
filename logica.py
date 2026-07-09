
#logica.py


import datos


def crear_tarea(descripcion):
    tarea = {"descripcion": descripcion, "completada": False}
    datos.guardar_tarea(tarea)
    return tarea


def listar_tareas():
    return datos.obtener_tareas()


def indice_valido(numero):
    tareas = datos.obtener_tareas()
    return 1 <= numero <= len(tareas)


def completar_tarea(numero):
    indice = numero - 1
    tarea = datos.obtener_tareas()[indice]
    tarea["completada"] = True
    return tarea


def eliminar_tarea(numero):
    indice = numero - 1
    return datos.eliminar_tarea_por_indice(indice)
