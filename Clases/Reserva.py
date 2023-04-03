"""from Cliente import *"""
"""from Habitacion import *"""
class Reserva:
    def __init__(self, id_reserva, num_doc, num_habitacion, precio_reserva, fecha_entrada, fecha_salida, metodos_pago):
        self.__id_reserva=id_reserva
        self.__num_doc=num_doc   #Llave foranea, recordar que hay que importar del otro modulo
        self.__num_habitacion=num_habitacion
        self.precio_reserva=precio_reserva
        self.fecha_entrada=fecha_entrada
        self.fecha_salida=fecha_salida
        self.metodos_pago=metodos_pago
    
    def getId(self):
        return self.__id_reserva
    
    def setId(self, id_reserva):
        self.__id_reserva=id_reserva
        
    def getNum_doc(self):
        return self.__num_doc
    
    def setNum_doc(self, num_doc):
        self.__num_doc=num_doc
        
    def getNum_hab(self):
        return self.__num_habitacion
    
    def setNum_hab(self, num_habitacion):
        self.__num_habitacion=num_habitacion
        
    def getPrecio(self):
        return self.precio_reserva
    
    def setPrecio(self, precio_reserva):
        self.precio_reserva=precio_reserva
    
    def getFecha_e(self):
        return self.fecha_entrada
    
    def setFecha_e(self, fecha_entrada):
        self.fecha_entrada=fecha_entrada
    
    def getFecha_s(self):
        return self.fecha_salida
    
    def setFecha_s(self, fecha_salida):
        self.fecha_salida=fecha_salida
        
    def getMetodo(self):
        return self.metodos_pago
    
    def setMetodo(self, metodos_pago):
        self.metodos_pago=metodos_pago