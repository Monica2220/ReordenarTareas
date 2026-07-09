"""
main.py
-------
Punto de entrada del programa.
Solo controla el bucle del menú y conecta las opciones con la interfaz.
"""

import interfaz


def main():
    while True:
        interfaz.mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            interfaz.accion_agregar()
        elif opcion == "2":
            interfaz.accion_ver()
        elif opcion == "3":
            interfaz.accion_completar()
        elif opcion == "4":
            interfaz.accion_eliminar()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
