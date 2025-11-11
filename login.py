import tkinter as tk 
from tkinter import messagebox
import menu

usuario_correcto = "aeromexico"
pass_correcto = "12345"

def mostrar_login():
    ventana_login = tk.Tk()
    ventana_login.title("login")
    ventana_login.geometry("300x200")
    ventana_login.config(bg=  "#e4f4fd")

   
    def verificar_login():
        usuario = entry_usuario.get()
        contraseña = entry_contraseña.get()
        

        if not usuario or not contraseña:
            messagebox.showwarning("Campos vacios", "Por favor, ingrese usuario y contraseña. ")
            return

        if usuario == usuario_correcto and contraseña == pass_correcto:
            messagebox.showinfo("Datos correctos", f"¡Bienvenido, {usuario}!")
            ventana_login.destroy()
            menu.abrir_menu()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    
    tk.Label(ventana_login, text="Usuario:",bg="#e4f4fd" ).pack(pady=5)
    entry_usuario = tk.Entry(ventana_login)
    entry_usuario.pack()
    entry_usuario.focus()
    
    tk.Label(ventana_login, text="Contraseña:", bg="#e4f4fd").pack(pady=5)
    entry_contraseña = tk.Entry(ventana_login, show="*")
    entry_contraseña.pack()
  

    tk.Button(ventana_login, text="Iniciar sesion", command=verificar_login, bg= "#72c8f1").pack(pady=10)

    tk.Button(ventana_login, text="Salir", command=ventana_login.destroy,bg= "#8bd3f8").pack(pady=5)

    ventana_login.mainloop()


if __name__ == "__main__":
    mostrar_login()