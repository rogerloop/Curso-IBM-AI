import tkinter as tk
from tkinter import messagebox


def calcular_regla_de_tres():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())

        # Regla de tres simple: a/b = c/x, entonces x = (b*c)/a
        x = (b * c) / a

        resultado_label.config(text=f"Resultado: {x:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero.")


# Crear la ventana principal
root = tk.Tk()
root.title("Regla de Tres Accesible")

# Configuración de accesibilidad
font_large = ("Arial", 18)
font_button = ("Arial", 16, "bold")

# Crear etiquetas y campos de entrada
label1 = tk.Label(root, text="Valor 1 (a):", font=font_large)
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry1 = tk.Entry(root, font=font_large, width=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Valor 2 (b):", font=font_large)
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry2 = tk.Entry(root, font=font_large, width=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Valor 3 (c):", font=font_large)
label3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry3 = tk.Entry(root, font=font_large, width=10)
entry3.grid(row=2, column=1, padx=10, pady=10)

# Botón para calcular
calcular_button = tk.Button(root, text="Calcular", font=font_button, command=calcular_regla_de_tres)
calcular_button.grid(row=3, column=0, columnspan=2, pady=20)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="Resultado:", font=font_large)
resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

# Hacer que el botón de calcular sea accesible con la tecla "Enter"
root.bind('<Return>', lambda event: calcular_regla_de_tres())

# Iniciar el loop principal
root.mainloop()
