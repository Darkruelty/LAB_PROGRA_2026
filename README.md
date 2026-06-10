# LAB_PROGRA_2026
Proyecto: Calculadora con Tkinter

Este proyecto consistió en el desarrollo de una calculadora Básica utilizando Python y la librería Tkinter. Aunque una calculadora parece un proyecto algo sencillo, implementarla correctamente me dejó múltiples aprendizajes clave, tanto a nivel técnico como en la lógica de programación.

1. Por qué evitar eval() y usar simpleeval
Uno de los puntos más importantes del proyecto fue la decisión de no usar la función eval() para evaluar las expresiones matemáticas. Aunque eval() es tentadora por su simplicidad, presenta graves desventajas:

- Seguridad: eval() puede ejecutar código arbitrario. Un usuario malintencionado podría ingresar comandos dañinos si la calculadora permitiera entrada libre.
- Rendimiento: Para operaciones repetitivas, eval() tiene un overhead significativo al compilar la cadena cada vez.
- Manejo de errores limitado: eval() lanza excepciones genéricas y no diferencia bien entre errores sintácticos, matemáticos (como división por cero) o de tipos.

Para solucionar esto, incorporé el módulo simpleeval, una alternativa segura y eficiente. Con simpleeval puedo:
- Evaluar únicamente expresiones matemáticas, sin riesgo de inyección de código.
- Controlar los operadores permitidos (+, -, *, /, **, etc.).
- Obtener errores más claros y manejables (por ejemplo: InvalidExpression).

Esta decisión no solo mejora la robustez del programa, sino que fue una excelente práctica para aprender a no confiar ciegamente en funciones nativas peligrosas y buscar alternativas profesionales.

2. Aprendiendo Tkinter: el desafío de las coordenadas

Trabajar con Tkinter fue todo un reto, especialmente el sistema de posicionamiento. Al principio intenté usar place() con coordenadas absolutas (x, y), lo que generaba problemas al redimensionar la ventana o en diferentes resoluciones de pantalla. Comprendí que:

- pack() es útil para disposiciones lineales simples (arriba-abajo o izquierda-derecha).
- grid() es más poderoso para calculadoras, porque permite organizar botones en filas y columnas de manera predecible. Aun así, entender los parámetros row, column, columnspan, sticky y padx/pady me tomó varios intentos y debugging visual.

3. Más aprendizajes adicionales

-Manejo de eventos: Asociar cada botón a una función que actualice la pantalla o realice el cálculo me ayudó a entender el modelo de programación dirigida por eventos (event-driven).
-Manejo de errores en la UI: Capturar excepciones de simpleeval y mostrar "Error" en la pantalla de la calculadora en lugar de que el programa colapse.
- Módulos y separación de responsabilidades: Dividí el código en funciones: una para manejar clics, otra para actualizar la pantalla, otra para evaluar, etc. Aunque el proyecto es pequeño, ya empiezo a ver la importancia de mantener el código organizado.

4. Reflexión final y próximos pasos
Este proyecto me dejó claro que Tkinter requiere práctica continua, especialmente en el sistema de layouts. Las coordenadas absolutas (place) son tentadoras al principio, pero no escalan. Me propongo a futuro:

- Hacer más proyectos con Tkinter (un cronómetro, un bloc de notas, un mini editor de texto) para dominar grid() y pack().
- Explorar ttk (Tkinter Themed Widgets) para mejorar la apariencia visual.
- Añadir funcionalidades extra a esta calculadora: historial de operaciones, botones de memoria (M+, M-, MR) o cambio de tema claro/oscuro.

