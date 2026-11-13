import email
import re
import tkinter as tk
from tkinter import messagebox

class FormularioRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Formulario de Registro")
        self.root.geometry("500x600")

        # Etiquetas y campos de entrada
        self.nombre = tk.StringVar()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.confirm_password = tk.StringVar()
        self.edad = tk.StringVar()
        self.genero = tk.StringVar(value="")
        self.acepto = tk.BooleanVar()

        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Registro de Usuario",
                 font=("Arial", 16, "bold")
                 ).grid(row=0, column=0, columnspan=2, pady=(0,15))

        campos = [
            ("Nombre Completo:", self.nombre,False),
            ("Email:", self.email,False),
            ("Contraseña:", self.password, True),
            ("Confirmar Contraseña:", self.confirm_password, True),
            ("Edad:", self.edad, False),
        ]

        for i, (label, var, oculto) in enumerate(campos):
            tk.Label(frame, text=label, anchor="e").grid(row=i+1, column=0, sticky="e", pady=5, padx=(0,10))
            entry = tk.Entry(
                   frame, textvariable=var, show="*" if oculto else "")
            entry.grid(row=i+1, column=1, pady=5, sticky="w")

        tk.Label(frame, text="Género:").grid(row=6, column=0, sticky="e", pady=5)
        genero_frame = tk.Frame(frame)
        genero_frame.grid(row=6, column=1, sticky="w")
        for opcion in ["Masculino", "Femenino", "Otro"]:
            tk.Radiobutton(
                genero_frame, text=opcion, variable=self.genero, value=opcion
            ).pack(side="left", padx=5)

        tk.Checkbutton(
            frame, text="Acepto los términos y condiciones", variable=self.acepto
        ).grid(row=7, column=0, columnspan=2, pady=10)

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=8, column=0, columnspan=2, pady=15)
        tk.Button(
            btn_frame, text="Registrar",
            command=self.validar,width=15,
            bg="#4CAF50", fg="white"
        ).pack(side="left", padx=10)
        tk.Button(
            btn_frame, text="Limpiar",
            command=self.limpiar, width=15
        ).pack(side="left", padx=10)

    def validar(self):
        errores = []
        if not self.nombre.get().strip():
            errores.append("El nombre es obligatorio.")
        
        email = self.email.get().strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
            errores.append("debe contener @ y el dominio")
        
        if len(self.password.get()) < 8:
            errores.append("La contraseña debe tener al menos 8 caracteres.")

        if self.password.get() != self.confirm_password.get():
            errores.append("Las contraseñas no coinciden.")
        
        try:
            edad = int(self.edad.get())
            if edad < 15 or edad > 99:
                errores.append("La edad debe estar entre 15 y 99 años.")
        except ValueError:
            errores.append("La edad debe ser un número válido.")

        if not self.genero.get():
            errores.append("Debe seleccionar un género.")

        if not self.acepto.get():
            errores.append("Debe aceptar los términos y condiciones.")

        if errores:
            messagebox.showerror(
                "Errores de Validación", "\n".join(errores))
        else:
            messagebox.showinfo(
                "Registro Exitoso",
                f"¡Bienvenido {self.nombre.get()}!\n"
                f"Email: {self.email.get()}\n"
            )

    def limpiar(self):
        for var in [self.nombre, self.email, self.password, self.confirm_password, self.edad, self.genero]:
            var.set("")
        self.acepto.set(False)

if __name__ == "__main__":
    app = FormularioRegistro()
    app.root.mainloop()