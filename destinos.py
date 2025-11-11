import tkinter as tk
from tkinter import ttk, messagebox
import conexion
import menu

def abrir_destinos():
    destinos = tk.Tk()
    destinos.title("Gestión de destinos")
    destinos.geometry("700x600")
    destinos.config(bg="#e4f4fd")
    
    campos = ["id_destino", "nombre_destino"]
    entradas = {}
    
    for i, texto in enumerate(campos):
        tk.Label(destinos, text=texto, bg="#e4f4fd").grid(row=i, column=0, padx=10, pady=5,sticky="w")
        entradas[texto] = tk.Entry(destinos)
        entradas[texto].grid(row=i, column=1, padx=10, pady=5)
    
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
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios")
            return
        sql = "INSERT INTO destinos (id_destino,nombre_destino) VALUES (%s, %s)"
        params = tuple(entradas[c].get() for c in campos)
        ejecutar_sql(sql, params)
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Éxito", "Destino agregado correctamente") 
        
    def actualizar():
        if not entradas["id_destino"].get():
            messagebox.showwarning("Atención", "Seleccione un destino para actualizar")
            return
        sql = "UPDATE destinos SET  nombre_destino=%s WHERE id_destino=%s"
        params = (entradas["nombre_destino"].get(), entradas["id_destino"].get())
        ejecutar_sql(sql, params)
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Éxito", "Destino actualizado correctamente") 
        
    def eliminar():
        if not entradas["id_destino"].get():
            messagebox.showwarning("Atencion", "Seleccione un destino para eliminar")
            return
        sql = "DELETE FROM destinos WHERE id_destino=%s"
        ejecutar_sql(sql, (entradas["id_destino"].get(),))
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Éxito", "Destino eliminado correctamente")     
        
    def limpiar():
        for e in entradas.values():
            e.delete(0, tk.END)
            
    def mostrar_datos():
        for row in tabla.get_children():
            tabla.delete(row)
        datos = ejecutar_sql("SELECT * FROM destinos", fetch=True)
        for fila in datos:
            tabla.insert("", tk.END, values=fila)
            
    def seleccionar(event):
        seleccionado = tabla.selection()
        if seleccionado:
            valores = tabla.item(seleccionado[0], "values")
            for i, c in enumerate(campos):
                entradas[c].delete(0, tk.END)
                entradas[c].insert(0, valores[i])
                
    botones = [("Agregar", insertar), ("Actualizar", actualizar), ("Eliminar", eliminar), ("Limpiar", limpiar)]
    for i, (texto, cmd) in enumerate(botones):
            tk.Button(destinos, text=texto, width=12, command=cmd,bg="#b4e3ff").grid(row=4, column=i, padx=10, pady=10)
            
    columnas = ("id_destino","nombre_destino")
    tabla = ttk.Treeview(destinos, columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.grid(row=5, column=0, columnspan=2, padx=10, pady=20)
    tabla.bind("<<TreeviewSelect>>", seleccionar)
    
    tk.Button(destinos, text="Regresar al Menu", width=20,
              command=lambda: [destinos.destroy(), menu.abrir_menu()],bg="#b4e3ff").grid(row=7, column=0, columnspan=2, pady=10)
        
    mostrar_datos()
    destinos.mainloop()   
    
if __name__ == "__main__":0
.213
abrir_destinos()      