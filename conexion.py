import  mysql.connector 
#mysql.connector sirve para que python realize conexiones con BD
from tkinter import messagebox
#messagebox es una funcion de la lbreria de tkinter

def connector_bd(): #definimos nuestra funcion para conectar 
    try:
        conn = mysql.connector.connect(
            host ="localhost", #Nombre del servidor333
            user = "root", #Nombre del usuario
            password = "12345678",#Contraseña
            database = "aeromexico"#Nombre de la base de datos
        )
        return conn #retornamos la conexion
    except mysql.connector.Error as err:

        messagebox.showerror("Error",f"No se puede establecerla conexion con la BD\n{err}")       
        return None
    #Si algo sale mal, err guardara exactamente que error se genero
    #mysql.connector.Error indica exactamente cual es el error
    #f"No se puede establecerla conexion con la BD\n{err}"
    #se muestra ese mensaje de error, junto con el error encontrado 
    #return None, si existe un error, devuelve None, asi el resto
    #del programa sabra que le fallo
    