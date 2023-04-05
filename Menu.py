from os import system as interfaz
import BD.Habitacion as BDh

try:
    while True:
        interfaz("cls")
        print("Bienvenido al menu \nPresione 1 para editar los datos de las habitaciones")
        pedir=int(input(' '))
        match pedir:
            case 1:
                while True:
                    interfaz("cls")
                    opcion=int(input("Oprima 1 si desea crear una nueva habitacion \nOprima 2 si desea actualizar los datos de una habitacion ya creada \nOprima 3 si desea consultar los datos de la tabla \nOprima 4 si desea eliminar una habitacion \nOprima 5 si desea volver al menu principal \n"))
                    match opcion:
                        case 1:
                            BDh.create()
                        case 2:
                            BDh.update()
                        case 3:
                            BDh.read()
                        case 4:
                            BDh.delete()
                        case 5:
                            break
                        case _:
                            print("Escoja una opcion valida")
                    interfaz("pause")
            case 0:
                break
            case _:
                print('El numero no es valido')
        interfaz("pause")
        print("Escoja un numero valido")
except (TypeError, ValueError) as e:
    print(type(e), e)