import tkinter as tk 
from tkinter import ttk, messagebox 
import conexion 
import menu

def abrir_vuelos(): 
    vuelos = tk.Tk() 
    vuelos.title("Gestion de vuelos") 
    vuelos.geometry("1600x900")
    vuelos.config(bg="#e4f4fd")
    
    campos = ["no_vuelo", "fecha_partida", "fecha_llegada", "clase_servicio", "no_aciento", "lugar_partida", "no_boleto", "id_empleado", "visa", "id_destino", "cantidad", "precio_unitario", "subtotal", "iva", "total"] 
    entradas = {} 
    
    for i, texto in enumerate(campos): 
        tk.Label(vuelos, text=texto,bg="#e4f4fd").grid(row=i, column=0, padx=30, pady=5,  sticky="w") 
        entradas[texto] = tk.Entry(vuelos) 
        entradas[texto].grid(row=i, column=1, padx=30, pady=5)
        
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
        sql = "INSERT INTO vuelos (no_vuelo, fecha_partida, fecha_llegada, clase_servicio, no_aciento, lugar_partida, no_boleto, id_empleado, visa, id_destino, cantidad, precio_unitario, subtotal, iva, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" 
        params = tuple(entradas[c].get() for c in campos) 
        ejecutar_sql(sql, params) 
        mostrar_datos()  
        limpiar() 
        messagebox.showinfo("exito", "vuelo agregado correctamente") 
        
    def actualizar(): 
        if not entradas["no_vuelo"].get(): 
            messagebox.showwarning("atencion", "Seleccione un vuelo para actualizar") 
            return 
        sql = "UPDATE vuelos SET fecha_partida=%s, fecha_llegada=%s, clase_servicio=%s, no_aciento=%s, " \
        "lugar_partida=%s, no_boleto=%s, id_empleado=%s, visa=%s, id_destino=%s, cantidad=%s, precio_unitario=%s, " \
        "subtotal=%s, iva=%s, total=%s where no_vuelo=%s" 
        params = (entradas["fecha_partida"].get(), entradas["fecha_llegada"].get(), 
                  entradas["clase_servicio"].get(), entradas["no_aciento"].get(), entradas["lugar_partida"].get(), entradas["no_boleto"].get(), 
                  entradas["id_empleado"].get(), entradas["visa"].get(), entradas["id_destino"].get(), entradas["cantidad"].get(), 
                  entradas["precio_unitario"].get(), entradas["subtotal"].get(), entradas["iva"].get(), entradas["total"].get(), 
                  entradas["no_vuelo"].get())
        
        ejecutar_sql(sql, params)
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "vuelo actualizado correctamente")
        
    def eliminar():
        if not entradas["no_vuelo"].get():
            messagebox.showwarning("Atencion", "Seleccione un vuelo para eliminar")
            return
        sql = "DELETE FROM vuelos WHERE no_vuelo=%s"
        ejecutar_sql(sql, (entradas["no_vuelo"].get(),))
        mostrar_datos()
        limpiar()
        messagebox.showinfo("Exito", "vuelos eliminado correctamente")
        
    def limpiar():
        for e in entradas.values():
            e.delete(0, tk.END)
            
    def mostrar_datos():
        for row in tabla.get_children():
            tabla.delete(row)
        datos = ejecutar_sql("SELECT * FROM vuelos", fetch=True)
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
        tk.Button(vuelos, text=texto, width=12, command=cmd, bg="#b4e3ff").grid(row=19, column=i,padx=10, pady=10)
        
    columnas = ("no_vuelo", "fecha_partida", "fecha_llegada", "clase_servicio", "no_aciento", "lugar_partida", "no_boleto", "id_empleado", "visa", "id_destino", "cantidad", "precio_unitario", "subtotal", "iva", "total")
    tabla = ttk.Treeview(vuelos , columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=100)
    tabla.grid(row=20, column=0, columnspan=15, padx=10, pady=20)
    tabla.bind("<<TreeviewSelect>>", seleccionar)
    
    tk.Button(vuelos, text="Regresar al Menu", width=20,
            command=lambda: [vuelos.destroy(), menu.abrir_menu()],bg="#b4e3ff").grid(row=25,column=0, columnspan=15, pady=10)
    
    mostrar_datos()
    vuelos.mainloop()
    
if __name__ == "__main__":
    abrir_vuelos()