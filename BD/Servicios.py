from sqlite3 import *
from sys import path as ruta
from os import system as interfaz


con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")

cursor1=con.cursor()

"""cursor1.execute("select * from Servicios where Num_Doc=12345")
ubicacion=12345
datos=cursor1.fetchall()[0]

costo_total= 0
for i in range(1,10):
    costo_total+=datos[i]
print(costo_total)

cursor1.execute("update Servicios set Costo_total =? where Num_Doc =?",(costo_total,ubicacion))

con.commit()"""


cursor1.execute("select Precio_habitacion, Costo_servicios from Habitacion as HB INNER JOIN Reserva as RE ON HB.Num_habitacion=RE.Num_habitacion where Num_Doc=12345")

datos2=cursor1.fetchall()[0]
ubicacion=12345

precio_reserva=0
for valor in datos2:
    precio_reserva+=valor

print(precio_reserva)

cursor1.execute("update Reserva set Precio_Reserva =? where Num_Doc =?",(precio_reserva,ubicacion))

con.commit()



