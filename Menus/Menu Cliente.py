#ATENCION: Este menu no es canonico dentro del sistema del programa debido a que las credenciales del cliente...
#... se agregan automaticamente en la base de datos cuando se ingresan los datos por medio de la pagina web en registro...
#... pero como no tenemos la pagina, este menu es provisional para crear datos del cliente.

#ATENCION: Cambiar la ruta de importacion del modulo de base de datos para su correcto funcionamiento.


from os import system as interfaz
from sys import path as ruta
ruta.append("C:\\Juez\\Proyecto_Final")
import BD.Cliente as BDc

try:
    while True:
        interfaz("cls")
        opcion=int(input("Bienvenido al menu \nOprima 1 si desea manejar los clientes \nOprima 2 para salir del programa \n"))
        match opcion:
            case 1:
                while True:
                    interfaz("cls")
                    opcionC=int(input("Oprima 1 si desea agregar un cliente nuevo \nOprima 2 si desea actualizar los datos de un cliente ya agregado \nOprima 3 para ver todos los datos de la tabla \nOprima 4 para eliminar a un cliente de la tabla \nOprima 5 para volver al menu principal \n"))
                    match opcionC:
                        case 1:
                            BDc.agregarcliente()
                        case 2:
                            BDc.actualizar()
                        case 3:
                            BDc.verdatos()
                        case 4:
                            BDc.delete()
                        case 5:
                            break
                        case _:
                            print("El numero no es valido")
                    interfaz("pause")
            case 2:
                break
            case _:
                print("El numero no es valido")
        interfaz("pause")
        print("Escoja un numero valido")
except (TypeError, ValueError) as e:
    print(type(e), e)