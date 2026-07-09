"""
interfaz.py
-----------
Responsabilidad: toda la interacción con el usuario.
Muestra menús y mensajes, lee lo que el usuario escribe y valida
la entrada. Llama a la lógica, pero no manipula los datos directamente.
"""

import logica


def mostrar_menu():
    print("\n===== SISTEMA DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")


def pedir_numero(mensaje):
    """
    Pide un número al usuario y controla el error si escribe texto.
    Devuelve el número (int) o None si la entrada no es válida.
    """
    entrada = input(mensaje)
    try:
        return int(entrada)
    except ValueError:
        print("Error: debes ingresar un número válido.")
        return None


def accion_agregar():
    descripcion = input("Escribe la descripción de la tarea: ").strip()
    if descripcion == "":
        print("Error: la descripción no puede estar vacía.")
        return
    tarea = logica.crear_tarea(descripcion)
    print(f"Tarea '{tarea['descripcion']}' agregada correctamente.")


def accion_ver():
    tareas = logica.listar_tareas()
    if len(tareas) == 0:
        print("No hay tareas registradas.")
        return

    print("\n--- Lista de tareas ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✔ Completada" if tarea["completada"] else "✘ Pendiente"
        print(f"{i}. {tarea['descripcion']} - {estado}")


def accion_completar():
    accion_ver()
    if len(logica.listar_tareas()) == 0:
        return

    numero = pedir_numero("\nIngresa el número de la tarea a completar: ")
    if numero is None:
        return
    if not logica.indice_valido(numero):
        print("Error: ese número de tarea no existe.")
        return

    tarea = logica.completar_tarea(numero)
    print(f"Tarea '{tarea['descripcion']}' marcada como completada.")


def accion_eliminar():
    accion_ver()
    if len(logica.listar_tareas()) == 0:
        return

    numero = pedir_numero("\nIngresa el número de la tarea a eliminar: ")
    if numero is None:
        return
    if not logica.indice_valido(numero):
        print("Error: ese número de tarea no existe.")
        return

    tarea = logica.eliminar_tarea(numero)
    print(f"Tarea '{tarea['descripcion']}' eliminada.")
