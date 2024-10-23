import tkinter as tk
from tkinter import ttk, messagebox
import json

# Leer el archivo JSON
with open('productos.json', 'r') as file:
    productos = json.load(file)

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Productos")
root.geometry("600x400")
root.configure(bg="#f4f4f4")

# Estilos para la tabla
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#4CAF50", foreground="white")
style.configure("Treeview", font=("Helvetica", 10), background="#f4f4f4", foreground="#333", rowheight=30)

# Crear la tabla
tabla = ttk.Treeview(root, columns=("ID", "NOMBRE", "DESCRIPCION", "PRECIO"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("NOMBRE", text="Nombre")
tabla.heading("DESCRIPCION", text="Descripción")
tabla.heading("PRECIO", text="Precio ($)")
tabla.column("ID", width=50, anchor=tk.CENTER)
tabla.column("NOMBRE", width=150, anchor=tk.W)
tabla.column("DESCRIPCION", width=250, anchor=tk.W)
tabla.column("PRECIO", width=100, anchor=tk.CENTER)

# Insertar los productos en la tabla
for producto in productos:
    tabla.insert("", tk.END, values=(producto["ID"], producto["NOMBRE"], producto["DESCRIPCION"], producto["PRECIO"]))

# Función para mostrar la información del producto en una ventana emergente
def mostrar_informacion(event):
    item = tabla.selection()[0]  # Obtener el item seleccionado
    producto = tabla.item(item, "values")  # Obtener los valores del item
    id_producto = producto[0]
    nombre_producto = producto[1]
    descripcion_producto = producto[2]
    precio_producto = producto[3]

    # Crear la ventana emergente
    ventana_emergente = tk.Toplevel(root)
    ventana_emergente.title("Detalles del Producto")
    ventana_emergente.geometry("300x200")
    ventana_emergente.configure(bg="#f4f4f4")

    # Etiquetas para mostrar la información
    tk.Label(ventana_emergente, text=f"ID: {id_producto}", font=("Helvetica", 12), bg="#f4f4f4").pack(pady=10)
    tk.Label(ventana_emergente, text=f"Nombre: {nombre_producto}", font=("Helvetica", 12), bg="#f4f4f4").pack(pady=10)
    tk.Label(ventana_emergente, text=f"Descripción: {descripcion_producto}", font=("Helvetica", 12), bg="#f4f4f4").pack(pady=10)
    tk.Label(ventana_emergente, text=f"Precio: ${precio_producto}", font=("Helvetica", 12), bg="#f4f4f4").pack(pady=10)

# Vincular el doble clic en la tabla a la función mostrar_informacion
tabla.bind("<Double-1>", mostrar_informacion)

# Agregar la tabla a la ventana
tabla.pack(pady=20)

# Iniciar la aplicación
root.mainloop()
