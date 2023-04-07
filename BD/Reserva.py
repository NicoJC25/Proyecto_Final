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
    Reserva=CR.Reserva()
    micursorcreate.execute()