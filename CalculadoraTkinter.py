import tkinter as tk
from simpleeval import simple_eval 
# Se instala con pip install simpleeval para que pueda ejecutar expresiones matemáticas de forma segura

#Función para agregar números a la entrada
def agregar_numero(numero):
    entrada.insert(tk.END, str(numero))

# Funciones para realizar las operaciones aritméticas básicas (+, -, *, y /)
# Estas funciones simplemente agregan el operador correspondiente a la entrada cuando se presiona el botón
# Asi tambien esta función es mas segura que usar eval() directamente, ya que simple_eval limita las operaciones 
# a las matemáticas básicas y no permite la ejecución de código arbitrario.
def realizar_operacion():
    try:
        expresion = entrada.get()
        
        # Reemplazar ^ por ** si es necesario (potencia)
        expresion = expresion.replace('^', '**')
        
        resultado = simple_eval(expresion)
        
        # Limitar decimales a 8 para evitar resultados con demasiados dígitos
        if isinstance(resultado, float):
            resultado = round(resultado, 8)
        
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

   

def limpiar():
    entrada.delete(0, tk.END)  # Borra todo el contenido del campo de entrada

    #crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

#creamos el campo de entrada

entrada = tk.Entry(ventana, font=("Arial", 20), justify="center",)
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Lista de botones con sus respectivas valores y la ubicación en la cuadrícula
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("**", 4, 2), ("+", 4, 3),
    ("(", 5, 0), (")", 5, 1)

    ]


# Creamos los botones y ubicamos en la cuadrícula
for valor, fila, columna in botones:
    boton = tk.Button(ventana, text=valor, font=("Arial", 20), command=lambda v=valor: agregar_numero(v))
    boton.grid(row=fila, column=columna, padx=5, pady=6, sticky="nsew")


# Creamos el botón para limpiar el campo de entrada
limpiar_boton = tk.Button(ventana, text="C", font=("Arial", 20), command=limpiar)
limpiar_boton.grid(row=5, column=2, padx=5, pady=5, columnspan=1, sticky="nsew")

# Creamos el botón de igual para obtener el resultado de la operación
calcular_boton = tk.Button(ventana, text="=", font=("Arial", 20), command=realizar_operacion)
calcular_boton.grid(row=5, column=3, padx=5, pady=5, columnspan=2, sticky="nsew")

#iniciamos el bucle principal de la aplicación
ventana.mainloop()
