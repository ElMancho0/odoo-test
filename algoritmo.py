import customtkinter as ctk

def exponenciacion_rapida_mod(base, exponent, modulo):
    resultado = 1
    while exponent > 0:
        if exponent % 2 == 1:
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        exponent //= 2
    return resultado

def calcular():
    try:
        base = int(base_entry.get())
        exponent = int(exponent_entry.get())
        modulus = int(modulus_entry.get())
        result = exponenciacion_rapida_mod(base, exponent, modulus)
        output_label.configure(text=f"Resultado: {result}")
    except ValueError:
        output_label.configure(text="Por favor, ingrese valores enteros válidos")

root = ctk.CTk()
root.title("Exponenciación Rápida con Módulo")
root.geometry("300x400")

base_label = ctk.CTkLabel(root, text="Ingrese la base:")
base_label.pack(pady=5)
base_entry = ctk.CTkEntry(root)
base_entry.pack(pady=5)

exponent_label = ctk.CTkLabel(root, text="Ingrese el exponente:")
exponent_label.pack(pady=5)
exponent_entry = ctk.CTkEntry(root)
exponent_entry.pack(pady=5)

modulus_label = ctk.CTkLabel(root, text="Ingrese el mod:")
modulus_label.pack(pady=5)
modulus_entry = ctk.CTkEntry(root)
modulus_entry.pack(pady=5)

calculate_button = ctk.CTkButton(root, text="Calcular", command=calcular)
calculate_button.pack(pady=20)

output_label = ctk.CTkLabel(root, text="Resultado:")
output_label.pack(pady=5)

root.mainloop()

# a = 3
# b = 61897001964269013744956215
# n = 618970019642690137449562111