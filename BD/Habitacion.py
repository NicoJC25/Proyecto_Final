from sqlite3 import *
from sys import path as ruta
import Clases.Habitacion as CH

ruta.append("C:\\Juez\\Proyecto_Final")

con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
"""con=connect("sqlite-tools/DB/Hotel.db")"""


def create():
    micursorcreate=con.cursor()
    numero_habitacion=int(input("Ingrese el numero de la habitacion a agregar: "))
    tipo_habitacion=input("Ingrese el tipo de la habitacion a agregar: ")
    precio_habitacion=int(input("Ingrese el precio de la habitacion a agregar: "))
    estado_habitacion=input("Ingrese el estado de la habitacion: ")
    Habit=CH.Habitacion(numero_habitacion,tipo_habitacion,precio_habitacion,estado_habitacion)
    create=(Habit.getNum(),Habit.getTipo(),Habit.getPrecio(),Habit.getEstado())
    micursorcreate.execute("insert into Habitacion values(?,?,?,?)", create)
    con.commit()
    con.close()

"""def update():
    micursorupdate=con.cursor()
    columna=input("¿Cual es la columna que desea actualizar?: ")
    if columna=="tipo_habitacion":
        tipo_habitacion=int(input("Ingrese el tipo de habitacion por el cual va a reemplazar el actual: "))
        ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
        update="""
        
'''def read():
    micursorread=con.cursor()'''
    
def delete():
    micursordelete=con.cursor()
    columna=int(input("Ingrese el id de la columna que quiera eliminar: "))
    


create()



#CODIGO COMENTADO

#Las primeras 3 lineas son modulos importados: El primero es sqlite, con este modulo se pueden sacar todas las funciones para manipular...
#... las bases de datos en Python. El segundo es sys que importa path, este se usara mas adelante para poder acceder a la carpeta de...
#... clases en forma de paquete. La tercera es la importacion del modulo Habitacion en el paquete de clases, renombrado para que...
#... al momento de usarlo, su nombre no se vea tan largo.

#Lo proximo es como se vio anteriormente, acceder al paquete de Clases mediante ruta absoluta.
#Luego, se nombra una variable que lleva dentro la funcion con. Esta funcion lo que hace es que recibe como argumento la ruta por la cual...
#... se accede a la base de datos, incluyendo el nombre de esta al final. De esta forma, se hace la conexion entre el archivo y...
#... la base de datos. Esta funcion pertenece al modulo de sqlite
#En forma de comentario se encuentra una version de la ruta pero relativa

#Vamos con la funcion de Create.
#Linea 11: Definimos la funcion que no recibe ningun argumento.
#Linea 12: Creamos un cursor. Un cursor es un metodo que permite la manipulacion de la base de datos. Se crea asignandole una variable...
#... luego el nombre con que es la variable que tiene la conexion, un punto y despues la palabra reservada "cursor".
#Linea 13-16: Como los datos son agregados por un usuario, entonces se le asigna una variabla a cada dato de la tabla.
#Linea 17: Aqui es donde hacemos uso de las clases. Creamos un objeto, en este caso llamado "Habit". Para asignarle el valor del objeto...
#... se usa el CH que es como se renombro el archivo de Habitacion en clases, seguido por un punto y se invoca la clase como tal...
#... luego, se le ponen como parametros las variables que utilizamos antes para cada dato, asi ya tenemos el objeto creado.
#Linea 18: Ahora bien, aunque ya tenemos el objeto, este no puede ser usado para subirse a la base de datos como esta ya que...
#... al ser un compuesto de los datos, no es un tipo de dato valido. Entonces creamos una nueva variable, en este caso llamada create...
#... que lo que va a hacer es, uno por uno y con ayuda de los getters, sacar los datos del objeto que se subiran a la base de datos...
#... para esto, se invoca el nombre del objeto "Habit", seguido de un punto y luego el nombre del metodo que se quiera usar, en este caso los getters...
#... de esta forma, ahora en una nueva variable los datos pasaron de pertenecer a un compuesto a ahora, ser una tupla.
#Linea 19: LLega el momento de agregar los datos a la base de datos. Aqui usamos una version simplificada del execute...
#... el execute es un metodo que se usa para ejecutar en la base de datos lo que se le ingrese como argumento. En este caso, crear una columna...
#... primero se escribe el nombre de la variable que contiene el cursor, seguido por un punto y luego por el nombre del metodo "execute"...
#... dentro de los parentesis vamos a escribir la sintaxis de lo que queremos ejecutar, en este caso decimos que dentro de la tabla...
#... habitacion inserte valores, pero en este caso se usa una forma diferente de agregar los datos. Se van a poner entre parentesis...
#... signos de interrogacion cerrados seguidos de comas. La cantidad de signos depende tambien de la cantidad de filas a las cuales...
#... se les va a crear datos. En este caso, la tabla trae 4 filas: Numero de habitacion, tipo de habitacion, precio y estado...
#... por lo cual, son 4 signos. La razon de implementar los signos es debido a que como la sintaxis del metodo execute en la forma...
#... que nos enseñaron en clase no funciona con tuplas, listas, datos externos, etc. Pues con estos signos indicamos que vamos...
#... a agregar datos, pero mas adelante y en una forma de datos diferente a str. Asi, se pueden agregar tuplas o listas que luego...
#... en la misma base de datos se van a dividir estos datos y ajustar correctamente. Finalmente, cerramos las comillas y luego de una coma...
#... adjuntamos la variable create que trae la tupla con los datos.
#Linea 20: Utilizamos un metodo que tampoco vimos en clase pero que es muy importante y es commit. Con commit, todos los cambios...
#... que hagamos a la base de datos son guardados. Asi cuando se agregue la nueva columna, queda guardada en la base sin ningun problema.
#Linea 21: Con close, cerramos la conexion del archivo con la base de datos. Tanto commit como close usan la variable con que tiene...
#... la conexion entre ambas partes.

#NOTAS:
#Recordar agregar el archivo init.py en la carpeta de clases para decirle a Python que es un paquete
#Al momento de usar cualquier metodo, poner los parentesis al final. Como por ejemplo los getters de la clase o los metodos de sqlite


#Lo demas del archivo aun no esta completo asi que aun no esta comentado, pero en cuanto lo haga, comentaré eso tambien