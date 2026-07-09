# Sistema de Gestión de Tareas (To-Do List)

Sistema de tareas en consola, refactorizado a partir de un script único
en un proyecto modular con separación de responsabilidades.

## Estructura del proyecto

| Módulo | Responsabilidad |
|--------|-----------------|
| `datos.py` | Almacena la lista de tareas y da acceso a ellas (guardar, obtener, eliminar). |
| `logica.py` | Lógica de negocio: crear, completar y eliminar tareas. Valida índices. |
| `interfaz.py` | Interacción con el usuario: menús, mensajes y lectura/validación de entradas. |
| `main.py` | Punto de entrada. Controla el bucle del menú. |

## Separación de responsabilidades

- **Datos**: solo guardan y devuelven información, no imprimen nada.
- **Lógica**: procesa las tareas usando los datos, sin usar `print` ni `input`.
- **Interfaz**: única capa que se comunica con el usuario.
- **Main**: conecta todo mediante el menú principal.

## Manejo de errores

- Si el usuario escribe texto en vez de un número, el programa avisa y no se cae
  (se controla con `try/except ValueError`).
- Si el número de tarea no existe, se muestra un mensaje de error.
- No se permite agregar tareas con descripción vacía.

## Cómo ejecutar

```bash
python main.py
```

## Autor

[Tu nombre]
