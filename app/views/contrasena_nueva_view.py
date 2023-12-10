from tkinter import Tk,ttk

from functions.password import generar_contrasena_randomica


def contrasena_nueva():
    raiz = Tk()

    raiz.title("ventana de prueba")
    raiz.resizable(True, False)
    raiz.iconbitmap("recursos/llaves.ico")
    raiz.geometry("750x600")
    raiz.config(bg="pink")

    contrasena_label = ttk.Label(text="")
    contrasena_label.place(x=320, y=250)

    crear_contrasena_btn = ttk.Button(text="Generar contraseña",
                                      command=lambda :generar_contrasena_randomica(15, contrasena_label))
    crear_contrasena_btn.place(x=320, y=220)


    raiz.mainloop()