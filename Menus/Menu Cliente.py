#ATENCION: Este menu no es canonico dentro del sistema del programa debido a que las credenciales del cliente...
#... se agregan automaticamente en la base de datos cuando se ingresan los datos por medio de la pagina web en registro...
#... pero como no tenemos la pagina,e ste menu es provisional para crear datos del cliente.

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
                            BDc.