"""
datos.py
--------
Responsabilidad: almacenar y dar acceso a los datos (la lista de tareas).
No sabe nada sobre cómo se muestran ni sobre la lógica de negocio.
"""

# Lista donde se guardan todas las tareas.
# Cada tarea es un diccionario: {"descripcion": str, "completada": bool}
tareas = []


def obtener_tareas():
    """Devuelve la lista completa de tareas."""
    return tareas


def guardar_tarea(tarea):
    """Agrega una nueva tarea a la lista."""
    tareas.append(tarea)


def eliminar_tarea_por_indice(indice):
    """Elimina y devuelve la tarea en la posición indicada."""
    return tareas.pop(indice)
