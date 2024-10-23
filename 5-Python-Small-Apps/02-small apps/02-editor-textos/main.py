import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    global current_file
    filepath = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")
    current_file = filepath

def save_file():
    global current_file
    if current_file:
        filepath = current_file
    else:
        filepath = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
    with open(filepath, "w", encoding="utf-8") as output_file:
        text = text_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")
    current_file = filepath
    show_saved_message()

def show_saved_message():
    saved_message.config(text="File saved successfully!")
    window.after(2000, clear_saved_message)  # Clear the message after 2 seconds

def clear_saved_message():
    saved_message.config(text="")

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

def copy_text():
    try:
        selected_text = text_edit.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected_text)
    except tk.TclError:
        pass

def paste_text():
    try:
        clipboard_text = window.clipboard_get()
        text_edit.insert(tk.INSERT, clipboard_text)
    except tk.TclError:
        pass

def cut_text():
    try:
        selected_text = text_edit.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected_text)
        text_edit.delete(tk.SEL_FIRST, tk.SEL_LAST)
    except tk.TclError:
        pass

window = tk.Tk()
window.title("Text Editor")

current_file = None

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

text_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

saved_message = tk.Label(window, text="", fg="green")
saved_message.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# Crear menú contextual
context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="Copy", command=copy_text)
context_menu.add_command(label="Paste", command=paste_text)
context_menu.add_command(label="Cut", command=cut_text)

# Vincular evento del clic derecho al menú contextual
text_edit.bind("<Button-2>", show_context_menu)  # Botón-2 para macOS
text_edit.bind("<Button-3>", show_context_menu)  # Botón-3 para otros sistemas operativos

window.mainloop()
