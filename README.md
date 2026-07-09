# Sistema de Gestión de Tareas 

Sistema de tareas en consola, separación de responsabilidades.

Estructura del proyecto:

datos.py--Almacena la lista de tareas y da acceso a ellas (guardar, obtener, eliminar). 
logica.py--crear, completar y eliminar tareas. 
interfaz.py--Interacción con el usuario: menús, mensajes y validación de entradas. 
main.py-Controla el  menú. 

Separación:

- Datos: solo guardan y devuelven información, no imprimen nada.
- Lógica: procesa las tareas usando los datos.
- Interfaz: capa única que se comunica con el usuario.
- Main: conecta todo mediante el menú principal.

Errores:

- Si el usuario escribe texto en vez de un número, el programa avisa.
- Si el número de tarea no existe, se muestra un mensaje de error.
- No se permite agregar tareas con descripción vacía.

Autora: Mónica Villaseñor Sanromán
