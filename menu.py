import tkinter as tk
import login 
import clientes
import destinos
import empleados
import vuelos


def abrir_menu():
    menu = tk.Tk()
    menu.title("Menu Principal")
    menu.geometry("300x400")
    menu.config(bg=  "#e4f4fd")

    def regresar_a_login():
        menu.destroy()
        login.mostrar_login()


    def abrir_clientes():
        menu.withdraw()
        ventana_clientes = clientes.abrir_clientes()
        ventana_clientes.wait_window()
        menu.deiconify()

    
    def abrir_destinos():
        menu.withdraw()
        ventana_destinos = destinos.abrir_destinos()
        ventana_destinos.wait_window()
        menu.deiconify()


    def abrir_empleados():
        menu.withdraw()
        ventana_empleados = empleados.abrir_empleados()
        ventana_empleados.wait_window()
        menu.deiconify()


    def abrir_vuelos():
        menu.withdraw()
        ventana_vuelos = vuelos.abrir_vuelos()
        ventana_vuelos.wait_window()
        menu.deiconify()
    tk.Label(menu, text="Bienvenidos al menu principal", font=("Arial", 14), bg=  "#e4f4fd").pack(pady=20)

    tk.Button(menu, text="Clientes", width=25, command=abrir_clientes, bg= "#abdefa").pack(pady=5)
    tk.Button(menu, text="Destinos", width=25, command=abrir_destinos,  bg= "#8bd3f8").pack(pady=5)
    tk.Button(menu, text="Empleados", width=25, command=abrir_empleados,  bg= "#72c8f1").pack(pady=5)
    tk.Button(menu, text="Vuelos", width=25, command=abrir_vuelos, bg= "#66bde6").pack(pady=5)
    tk.Button(menu, text="Cerrar sesion", width=25, command=regresar_a_login,  bg= "#5ab2da").pack(pady=20)

    menu.mainloop()

if __name__ =="__main__":
    abrir_menu()





    


    


    
