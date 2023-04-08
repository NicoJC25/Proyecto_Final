from sqlite3 import *
from sys import path as ruta
from os import system as interfaz

ruta.append("C:\\Juez\\Proyecto_Final")
import Clases.Reserva as CR



def create():
    con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
    
    micursorcreate=con.cursor()
    numero_documento=int(input("Ingrese el numero de documento del cliente: "))
    numero_habitacion=int(input("Ingrese el numero de habitacion reservada: "))
    fecha_entrada=input("Ingrese la fecha de comienzo de la reserva: ")
    fecha_salida=input("Ingrese la fecha de finalizacion de la reserva: ")
    costo_servicios=int(input("Ingrese el costo total de los servicios: "))
    metodo_pago=input("Ingrese el metodo de pago seleccionado: ")
    
    micursorcreate.execute("insert into Reserva (Num_Doc, Num_habitacion, Fecha_Entrada, Fecha_Salida, Costo_servicios, Metodos_Pago) values (?,?,?,?,?,?)",(numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,metodo_pago))
    con.commit()
    
    micursorcreate.execute("select ID_Reserva from Reserva where Num_Doc =? and Num_habitacion =? and Fecha_Entrada =? and Fecha_Salida =? and Costo_servicios =? and Metodos_Pago =?",(numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,metodo_pago))
    dato=micursorcreate.fetchone()
    for i in dato:
        id_reserva=i
    
    micursorcreate.execute("select Precio_habitacion, Costo_servicios from Habitacion as HB INNER JOIN Reserva as RE ON HB.Num_habitacion=RE.Num_habitacion where ID_Reserva=?",id_reserva)
    datos2=micursorcreate.fetchall()[0]
    ubicacion=id_reserva

    precio_reserva=0
    for valor in datos2:
        precio_reserva+=valor
        
    micursorcreate.execute("update Reserva set Precio_Reserva =? where ID_Reserva =?",(precio_reserva,ubicacion))

    con.commit()

    Reserva=CR.Reserva(id_reserva,numero_documento,numero_habitacion,fecha_entrada,fecha_salida,costo_servicios,precio_reserva,metodo_pago)
    
    print("Reserva creada con exito :D")
    
    con.close()
create()
