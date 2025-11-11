import tkinter as tk 
from tkinter import ttk, messagebox 
import conexion 
import menu

def abrir_clientes():
    clientes = tk.Tk() 
    clientes.title("Gestion de clientes") 
    clientes.geometry("1000x600") 
    clientes.config(bg="#e4f4fd")

    campos = ["Visa", "Nombre del cliente", "Direccion", "Pasaporte", "Edad del cliente", "Numero de contacto"] 
    entradas = {} 

    for i, texto in enumerate(campos): 
        tk.Label(clientes, text=texto, bg="#e4f4fd").grid(row=i, column=0, padx=10, pady=5,  sticky="w",) 
        entradas[texto] = tk.Entry(clientes) 
        entradas[texto].grid(row=i, column=1, padx=20, pady=5,)  

    def ejecutar_sql(sql, params=(), fetch=False): 
        con = conexion.connector_bd() 
        cursor = con.cursor() 
        cursor.execute(sql, params)  
        if fetch: 
            resultado = cursor.fetchall() 
            con.close() 
            return resultado 
        else: 
            con.commit() 
            con.close() 

    def insertar(): 
        if any(not entradas[c].get() for c in campos): 
                messagebox.showwarning("Campos vacios", "Todos los campos son obligatorios")  
                return  
        sql = "INSERT INTO clientes (visa, nombre_cliente, direccion, pasaporte, edad_cli, no_contacto) VALUES (%s, %s, %s, %s, %s, %s)"
        params = tuple(entradas[c].get() for c in campos) 
        ejecutar_sql(sql, params) 
        mostrar_datos()  
        limpiar() 
        messagebox.showinfo("Exito", "Cliente agregado correctamente") 

    def actualizar(): 
        if not entradas["Visa"].get(): 
            messagebox.showwarning("Atencion", "Seleccione un cliente para actualizar") 
            return 
        sql = "UPDATE clientes SET nombre_cliente=%s, direccion=%s, pasaporte=%s, edad_cli=%s, no_contacto=%s WHERE visa=%s" 
        params = (entradas["Nombre del cliente"].get(), entradas["Direccion"].get(), entradas["Pasaporte"].get(), entradas["Edad del cliente"].get(), entradas["Numero de contacto"].get(), entradas["Visa"].get())

        ejecutar_sql(sql, params)
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "Cliente actualizado correctamente")

    def eliminar():
        if not entradas["Visa"].get():
            messagebox.showwarning("Atencion", "Seleccione un cliente para eliminar")
            return
        sql = "DELETE FROM clientes WHERE visa=%s"
        ejecutar_sql(sql, (entradas["Visa"].get(),))
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "Cliente eliminado correctamente")

    def limpiar():
        for e in entradas.values():
            e.delete(0, tk.END)

    def mostrar_datos():
        for row in tabla.get_children():
            tabla.delete(row)
        datos = ejecutar_sql("SELECT * FROM clientes", fetch=True)
        for fila in datos:
            tabla.insert("", tk.END, values=fila)
    
    def seleccionar(event):
        seleccionado = tabla.selection()
        if seleccionado:
            valores = tabla.item(seleccionado[0], "values")
            for i, c in enumerate(campos):
                entradas[c].delete(0, tk.END)
                entradas[c].insert(0, valores[i])
    
    botones = [("Agregar", insertar), ("Actualizar", actualizar), ("Eliminar",eliminar), ("Limpiar", limpiar)]
    for i, (texto, cmd) in enumerate(botones):
        tk.Button(clientes, text=texto, width=10, command=cmd, bg="#b4e3ff").grid(row=7, column=i,padx=10, pady=10)            

    columnas = ("Visa", "Nombre del cliente", "Direccion", "Pasaporte", "Edad del cliente", "Numero de contacto")
    tabla = ttk.Treeview(clientes, columns=columnas, show="headings", height=12 )
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
        
    tabla.grid(row=10, column=0, columnspan=6, padx=10, pady=20)
    tabla.bind("<<TreeviewSelect>>", seleccionar)
  

    tk.Button(clientes, text="Regresar al Menu", width=20,
            command=lambda: [clientes.destroy(), menu.abrir_menu()],bg="#b4e3ff").grid(row=15,column=0, columnspan=6, pady=10)
    
    mostrar_datos()
    clientes.mainloop()

if __name__ == "__main__":
    abrir_clientes()


