import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            expression = entry_var.get()
            result = eval(expression)
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Erro", "Expressão inválida")
    else:
        entry_var.set(entry_var.get() + button_text)

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.resizable(False, False)

# Aplicando fundo azul gradiente
root.configure(bg="#87CEFA")

# Campo de exibição
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), justify='right', bd=10, relief=tk.RIDGE, bg="#1E90FF", fg="white")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)

# Layout dos botões
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

frame_buttons = tk.Frame(root, bg="#87CEFA")
frame_buttons.pack()

button_colors = {"C": "#FF6347", "=": "#32CD32", "+": "#4682B4", "-": "#4682B4", "*": "#4682B4", "/": "#4682B4"}

def get_button_color(text):
    return button_colors.get(text, "#1E90FF")

for row_values in buttons:
    row_frame = tk.Frame(frame_buttons, bg="#87CEFA")
    row_frame.pack(expand=True, fill="both")
    for btn_text in row_values:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 18), width=5, height=2, bg=get_button_color(btn_text), fg="white",
                        command=lambda b=btn_text: on_click(b))
        btn.pack(side="left", expand=True, fill="both")

# Rodando a aplicação
root.mainloop()
