#Juan Esteban

from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\PINZON\Proyecto_Final")
import Clases.Administrador as CA
import Clases.Mesero as CM
import Clases.Recepcionista as CR

def create():
    con=connect("C:\PINZON\sqlite-tools-win32-x86-3400100\DB\Hotel.db")
    cursorcreate=con.cursor()
    numero_habitacion=int(input("Ingrese el numero de la habitacion a agregar: "))
    tipo_habitacion=input("Ingrese el tipo de la habitacion a agregar: ")
    precio_habitacion=int(input("Ingrese el precio de la habitacion a agregar: "))
    estado_habitacion=input("Ingrese el estado de la habitacion: ")
    Habit=CA.admin(numero_habitacion,tipo_habitacion,precio_habitacion,estado_habitacion)
    create=(Habit.getNum(),Habit.getTipo(),Habit.getPrecio(),Habit.getEstado())
    cursorcreate.execute("insert into Habitacion values(?,?,?,?)", create)
    con.commit()
    con.close()


def register():
    con1=connect("C:\PINZON\sqlite-tools-win32-x86-3400100\DB\Hotel.db")
    cursorregister=con1.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo administrador: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo administrador: ")
    Apellidos=input("Ingrese los apellidos del nuevo administrador: ")
    Email=input("ingrese el Correo electronico del nuevo administrador: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo administrador: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo administrador: ")
    Reg=CA.admin(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    register=(Reg.getNum_doc(),Reg.getTipo_doc(),Reg.getNombres(),Reg.getApellidos(),Reg.getEmail(),Reg.getContraseña(),Reg.getFunciones())
    cursorregister.execute("insert into Administrador values(?,?,?,?,?,?,?)", register)
    con1.commit()
    con1.close()
    
def registermesero():
    con2=connect("C:\PINZON\sqlite-tools-win32-x86-3400100\DB\Hotel.db")
    cursormesero=con2.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo mesero: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo mesero: ")
    Apellidos=input("Ingrese los apellidos del nuevo mesero: ")
    Email=input("ingrese el Correo electronico del nuevo mesero: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo mesero: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo mesero: ")
    Reg2=CM.Mesero(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    RegMesero=(Reg2.getNum_doc(),Reg2.getTipo_doc(),Reg2.getNombres(),Reg2.getApellidos(),Reg2.getEmail(),Reg2.getContraseña(),Reg2.getFunciones())
    cursormesero.execute("insert into Mesero values (?,?,?,?,?,?,?)", RegMesero)
    con2.commit()
    con2.close()

#NOTA IMPORTANTE: ESTA FUNCION PARA REGISTRAR RECEPCIONISTA SOLO FUNCIONARA SI LA CLASE RECPECIONISTA ESTA CREADA AL MOMENTO DE ESCRIBIR ESTE PROGRAMA LA CLASE NO ESTABA HECHA POR LO TANTO NO
#SE RECOMIENDA SU EJECUCION SIN LA COMPOROBACION DE LA CLASE RECEPCIONISTA
def registerRecepcionista():
    con3=connect("C:\PINZON\sqlite-tools-win32-x86-3400100\DB\Hotel.db")
    cursorRecepcionista=con3.cursor()
    Numero_Documento=int(input("ingrese el numero de documento del nuevo mesero: "))
    Tipo_Documento=input("ingrese el tipo del documento: ")
    Nombres=input("ingrese los nombres del nuevo mesero: ")
    Apellidos=input("Ingrese los apellidos del nuevo mesero: ")
    Email=input("ingrese el Correo electronico del nuevo mesero: ")
    Contraseña=input("ingrese la contraseña que desea para la cuenta del nuevo mesero: ")
    Funciones=input("Ingrese las funciones que podra tener el nuevo mesero: ")
    Reg3=CR.Recepcionista(Numero_Documento,Tipo_Documento,Nombres,Apellidos,Email,Contraseña,Funciones)
    RegRecepcionista=(Reg3.getNum_doc(),Reg3.getTipo_doc(),Reg3.getNombres(),Reg3.getApellidos(),Reg3.getEmail(),Reg3.getContraseña(),Reg3.getFunciones())
    cursorRecepcionista.execute("insert into Mesero values (?,?,?,?,?,?,?)", RegRecepcionista)
    con3.commit()
    con3.close()


