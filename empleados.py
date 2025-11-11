import tkinter as tk
from tkinter import ttk, messagebox 
import conexion 
import menu

def abrir_empleados():
    empleados= tk.Tk() 
    empleados.title("Gestion de empleados") 
    empleados.geometry("1000x600") 
    empleados.config(bg="#e4f4fd")

    campos =["id_empleado", "nombre_empleado", "no_contacto", "edad_em", "puesto"] 
    entradas = {} 

    for i, texto in enumerate(campos):
        tk.Label(empleados, text=texto,bg="#e4f4fd").grid(row=i, column=0, padx=10, pady=5,  sticky="w") 
        entradas[texto] = tk.Entry(empleados) 
        entradas[texto].grid(row=i, column=1, padx=20, pady=5) 

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
        sql = "INSERT INTO empleados (id_empleado, nombre_empleado, no_contacto, edad_em, puesto) VALUES (%s, %s, %s, %s, %s)"
        params = tuple(entradas[c].get() for c in campos) 
        ejecutar_sql(sql, params) 
        mostrar_datos()  
        limpiar() 
        messagebox.showinfo("Exito", "Empleado agregado correctamente") 

    def actualizar(): 
        if not entradas["id_empleado"].get(): 
            messagebox.showwarning("Atencion", "Seleccione un empleado para actualizar") 
            return 
        sql = "UPDATE empleados SET nombre_empleado=%s, no_contacto=%s, edad_em=%s, puesto=%s WHERE id_empleado=%s" 
        params = (entradas["nombre_empleado"].get(), entradas["no_contacto"].get(), entradas["edad_em"].get(), entradas["puesto"].get(), entradas["id_empleado"].get())
    
        ejecutar_sql(sql, params)
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "Empleado actualizado correctamente")

    def eliminar():
        if not entradas["id_empleado"].get():
            messagebox.showwarning("Atencion", "Seleccione un empleado para eliminar")
            return
        sql = "DELETE FROM empleados WHERE id_empleado=%s"
        ejecutar_sql(sql, (entradas["id_empleado"].get(),))
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "Empleado eliminado correctamente")

    def limpiar():
        for e in entradas.values():
            e.delete(0, tk.END)

    def mostrar_datos():
        for row in tabla.get_children():
            tabla.delete(row)
        datos = ejecutar_sql("SELECT * FROM empleados", fetch=True)
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
        tk.Button(empleados, text=texto, width=10, command=cmd, bg="#b4e3ff").grid(row=7, column=i,padx=10, pady=10)            

    columnas = ("id_empleado", "nombre_empleado", "no_contacto", "edad_em", "puesto")
    tabla = ttk.Treeview(empleados, columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.grid(row=10, column=0, columnspan=5, padx=10, pady=20)
    tabla.bind("<<TreeviewSelect>>", seleccionar)

    tk.Button(empleados, text="Regresar al Menu", width=20,
            command=lambda: [empleados.destroy(), menu.abrir_menu()] ,bg="#b4e3ff").grid(row=15,column=0, columnspan=5, pady=10)

    mostrar_datos()
    empleados.mainloop()

if __name__ == "__main__":
    abrir_empleados()



























