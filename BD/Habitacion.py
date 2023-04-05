from sqlite3 import *
from sys import path as ruta
from os import system as interfaz


ruta.append("C:\\Juez\\Proyecto_Final")
import Clases.Habitacion as CH





def create():
    con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
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

def update():
    while True:
        interfaz("cls")
        con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
        micursorupdate=con.cursor()
        print("¿Cual es la columna que desea actualizar? \nOprima 1 para editar el tipo de habitacion \nOprima 2 para editar el precio de habitacion \nOprima 3 para editar el estado de habitacion \nOprima 4 para salir de este apartado ")
        pedir=(int(input(' ')))
        match pedir:
            case 1:
                tipo_habitacion=input("Ingrese el tipo de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Tipo_habitacion =? where Num_habitacion =?",(tipo_habitacion,ubicacion))
                con.commit()
                con.close()
            case 2:
                precio_habitacion=int(input("Ingrese el precio de habitacion por el cual va a reemplazar el actual: "))
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Precio_habitacion =? where Num_habitacion =?",(precio_habitacion,ubicacion))
                con.commit()
                con.close()
            case 3:
                estado_habitacion=input("Ingrese el estado de habitacion por el cual va a reemplazar el actual: ")
                ubicacion=int(input("Ahora ingrese el id de habitacion de la cual va a cambiar el tipo de habitacion: "))
                micursorupdate.execute("update Habitacion set Estado_habitacion =? where Num_habitacion =?",(estado_habitacion,ubicacion))
                con.commit()
                con.close()
            case 4:
                break
            case _:
                print("Escoja un numero valido")
        interfaz("pause")

def read():
    con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
    micursorread=con.cursor()
    micursorread.execute("Select * from Habitacion")
    datos=micursorread.fetchall()
    print("Estos son los datos almacenados en la tabla de habitaciones: ")
    for fila in datos:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print("*"*50)
    con.commit()
    con.close()
    
def delete():
    con=connect("C:\\Juez\\sqlite-tools\\db\\Hotel.db")
    micursordelete=con.cursor()
    numero=int(input("Ingrese el numero de la habitacion que quiera eliminar: "))
    tipo=input("Ingrese el tipo de habitacion seleccionada: ")
    precio=int(input("Ingrese el precio de la habitacion seleccionada: "))
    estado=input("Ingrese el estado de la habitacion seleccionada: ")
    micursordelete.execute("delete from Habitacion where Num_habitacion =? and Tipo_habitacion=? and Precio_habitacion=? and Estado_habitacion=?",(numero,tipo,precio,estado))
    con.commit()
    con.close()



#CODIGO COMENTADO

#Las primeras 3 lineas son modulos importados: El primero es sqlite, con este modulo se pueden sacar todas las funciones para manipular...
#... las bases de datos en Python. El segundo es sys que importa path, este se usara mas adelante para poder acceder a la carpeta de...
#... clases en forma de paquete. La tercera es el modulo sys, que con este se puede realizar un menu de forma optima y bien organizado.

#Lo proximo es como se vio anteriormente, acceder al paquete de Clases mediante ruta absoluta para luego importar el modulo de...
#... habitacion. Primero se usa la ruta ya que importar el paquete antes genera un error.


#Vamos con la funcion de Create.
#Linea 13: Definimos la funcion que no recibe ningun argumento.
#Linea 14: Se nombra una variable que lleva dentro la funcion con. Esta funcion lo que hace es que recibe como argumento la ruta por la cual...
#... se accede a la base de datos, incluyendo el nombre de esta al final. De esta forma, se hace la conexion entre el archivo y...
#... la base de datos. Esta funcion pertenece al modulo de sqlite.
#Linea 15: Creamos un cursor. Un cursor es un metodo que permite la manipulacion de la base de datos. Se crea asignandole una variable...
#... luego el nombre con que es la variable que tiene la conexion, un punto y despues la palabra reservada "cursor".
#Linea 16-19: Como los datos son agregados por un usuario, entonces se le asigna una variabla a cada dato de la tabla.
#Linea 20: Aqui es donde hacemos uso de las clases. Creamos un objeto, en este caso llamado "Habit". Para asignarle el valor del objeto...
#... se usa el CH que es como se renombro el archivo de Habitacion en clases, seguido por un punto y se invoca la clase como tal...
#... luego, se le ponen como parametros las variables que utilizamos antes para cada dato, asi ya tenemos el objeto creado.
#Linea 21: Ahora bien, aunque ya tenemos el objeto, este no puede ser usado para subirse a la base de datos como esta ya que...
#... al ser un compuesto de los datos, no es un tipo de dato valido. Entonces creamos una nueva variable, en este caso llamada create...
#... que lo que va a hacer es, uno por uno y con ayuda de los getters, sacar los datos del objeto que se subiran a la base de datos...
#... para esto, se invoca el nombre del objeto "Habit", seguido de un punto y luego el nombre del metodo que se quiera usar, en este caso los getters...
#... de esta forma, ahora en una nueva variable los datos pasaron de pertenecer a un compuesto a ahora, ser una tupla.
#Linea 22: LLega el momento de agregar los datos a la base de datos. Aqui usamos una version simplificada del execute...
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
#Linea 23: Utilizamos un metodo que tampoco vimos en clase pero que es muy importante y es commit. Con commit, todos los cambios...
#... que hagamos a la base de datos son guardados. Asi cuando se agregue la nueva columna, queda guardada en la base sin ningun problema.
#Linea 24: Con close, cerramos la conexion del archivo con la base de datos. Tanto commit como close usan la variable con que tiene...
#... la conexion entre ambas partes.


#Funcion de update:
#Linea 27: Definir funcion
#Linea 28: Bucle infinito. Debido a que la funcion de update debe permitir actualizar cualquier dato de la tabla, entonces se crea un sub-menu...
#... dentro de la funcion para poder seleccionar que dato se quiere actualizar. Con el bucle se hace que siempre se permita dar las opciones...
#... hasta que el mismo usuario decida salir de este menu.
#Linea 29: Uso del modulo de sys para indicar que cada vez que el bucle del menu se repita, la consola se limpie automaticamente y...
#... elimine todo lo que salia en pantalla anteriormente para evitar confusiones.
#Linea 30: Se realiza la conexion a la base de datos de nuevo. Debido a que cuando se acaba cada proceso, se cierra la base de datos...
#... al entrar en otra funcion como es en este caso update, esa conexion ya no esta abierta, asi que hay que volver a abrirla para...
#... seguir realizando acciones en la base de datos.
#Linea 31: Se indica que micrusorupdate es la variable que va a tener la opcion de poder editar la base de datos como vimos con micursorcreate.
#Linea 32: Un print que muestra el menu en pantalla
#Linea 33: La variable input que va a pedir cual opcion del menu se va a seleccionar.
#Linea 34: Se utiliza el metodo match para que cuando se seleccione una opcion, se haga cierta instruccion dada.
#Linea 35-40: Si la opcion seleccionada es 1, entonces se va a editar el tipo de habitacion de alguna columna. En este caso se va a crear...
#... un input para indicar cual va a ser el valor por el que se va a reemplazar esa casilla y luego otro input para seleccionar...
#... cual columna va a ser, en este caso por medio del numero de habitacion al ser un dato unico. Luego, se va a usar el cursor...
#... junto con el metodo execute para mandar a la base de datos lo que se va a realizar. Recordar el uso de los signos de interrogacion...
#... para indicar que ese dato se va a definir luego y en este caso, al ser datos por separados los que se definen luego, despues de...
#... cerrar las comillas y seguido de la coma, se pone entre parentesis el orden de los datos que se van a reemplazar por cada signo...
#... de interrogacion, cada dato dividido por una coma entre esos parentesis. Finalmente, commit para guardar proceso y close para...
#... cerrar la base de datos.
#Linea 41-46: Se repite el proceso anterior pero actualizando el precio de alguna habitacion. Si la opcion escogida es 2, pedira...
#... por medio de un input el precio nuevo y la ubicacion de la habitacion a la que se le va a actualizar el precio. Luego...
#... ejecutara por medio del cursor lo anteriormente indicado, incluyendo los signos de interrogacion cerrados para indicar...
#... que ese dato se definira luego, en la tupla que esta ubicada luego de las comillas como vimos anteriormente. Finalmente...
#... commit y close.
#Linea 47-52: Si la opcion elegida es 3, se actualizara el estado de la habitacion. Por medio de un input pide el nuevo precio...
#... y por otro la habitacion a la que se le va a actualizar. Luego, con execute se ejecuta el proceso siguiendo la sintaxis...
#... de las comillas y finalmente commit y close.
#Lineas 53 y 54: Si la opcion elegida es 4, saldra de ese menu de update.
#Lineas 55 y 56: Si la opcion elegida es un numero completamente diferente, pedira un numero valido.
#Linea 57: Se usa de nuevo el modulo sys con la funcion interfaz para indicar que cuando acabe un proceso, salga un mensaje...
#... para que el usuario presione cualquier boton antes de continuar con el siguiente proceso.


#Funcion de read:
#Linea 58: Se crea la funcion
#Linea 59: Se abre la conexion entre el archivo y la base de datos.
#Linea 60: Se crea el cursor para editar la base de datos.
#Linea 61: Se ejecuta el codigo. En este caso no se usa alguna variable o algo por el estilo ya que es solo seleccionar la tabla...
#... y luego mostrarla en pantalla, lo que solo requiere sintaxis del mismo sqlite.
#Linea 62: Con la lista datos lo que se hace en conjunto con el metodo fetchall es seleccionar todos los datos sacados...
#... y guardarlos en esa lista.
#Linea 63: Un print que indica que a continuacion se veran los datos de la tabla
#Linea 64-69: Se crea un bucle for que lo que va a hacer es imprimir cada dato de la lista un por uno pero juntos, imprimiendo...
#... cada posicion de la lista que representa una fila. Luego se va a hacer una division de que luego de sacar una columna...
#... se va a hacer un separador con asteriscos entre cada una de estas.
#Linra 70: Commit para guardar los cambios.
#Linea 71: Se cierra la conexion.


#Funcion de delete:
#Linea 73: Se crea la funcion.
#Linea 74: Se abre la conexion.
#Linra 75: Se crea un cursor para editar la base de datos
#Linea 76-79: Debido a que para eliminar una columna especifica de la tabla se necesita especificar cada campo de la columna...
#... se hacen inputs para pedir cada dato de la columna.
#Linea 80: Se utiliza el metodo execute para ejecutar la accion. Entonces se escribe la parte de sintaxis de sqlite en conjunto...
#... con los signos de interrogacion para luego de forma externa indicar en su debido orden cuales son los datos que van en cada signo.
#Linea 81: Commit para guardar los cambios.
#Linea 82: Se cierra la conexion.


#NOTAS:
#Recordar agregar el archivo init.py en la carpeta de clases para decirle a Python que es un paquete
#Al momento de usar cualquier metodo, poner los parentesis al final. Como por ejemplo los getters de la clase o los metodos de sqlite
