"""
logica.py
---------
Responsabilidad: la lógica de negocio del sistema.
Crea, completa y elimina tareas usando el módulo de datos.
No hace print ni input: solo procesa y devuelve resultados.
"""

import datos


def crear_tarea(descripcion):
    """Crea una tarea nueva y la guarda. Devuelve la tarea creada."""
    tarea = {"descripcion": descripcion, "completada": False}
    datos.guardar_tarea(tarea)
    return tarea


def listar_tareas():
    """Devuelve la lista de tareas."""
    return datos.obtener_tareas()


def indice_valido(numero):
    """Verifica que el número corresponda a una tarea existente."""
    tareas = datos.obtener_tareas()
    return 1 <= numero <= len(tareas)


def completar_tarea(numero):
    """
    Marca como completada la tarea indicada (numero empieza en 1).
    Devuelve la tarea modificada.
    """
    indice = numero - 1
    tarea = datos.obtener_tareas()[indice]
    tarea["completada"] = True
    return tarea


def eliminar_tarea(numero):
    """
    Elimina la tarea indicada (numero empieza en 1).
    Devuelve la tarea eliminada.
    """
    indice = numero - 1
    return datos.eliminar_tarea_por_indice(indice)
