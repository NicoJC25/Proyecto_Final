#Juan Esteban

class Mesero:
    def __init__(self,Num_doc,Tipo_doc,Nombres,Apellidos,Email,Contraseña,Funciones):
        self.__Num_doc=Num_doc
        self.__Tipo_doc=Tipo_doc
        self.__Nombres=Nombres
        self.__Apellidos=Apellidos
        self.__Email=Email
        self.__Contraseña=Contraseña
        self.__Funciones=Funciones

    def getNum_doc(self):
          return self.__Num_doc

    def setNum_doc(self,Num_doc):
          self.__Num_doc=Num_doc   

    def getTipo_doc(self):
          return self.__Tipo_doc

    def setTipo_doc(self,Tipo_doc):
          self.__Tipo_doc=Tipo_doc    

    def getNombres(self):
          return self.__Nombres

    def setNombres(self,Nombres):
          self.__Nombres=Nombres

    def getApellidos(self):
          return self.__Apellidos

    def setApellidos(self,Apellidos):
          self.__Apellidos=Apellidos

    def getEmail(self):
          return self.__Email

    def setEmail(self,Email):
          self.__Email=Email

    def getContraseña(self):
          return self.__Contraseña

    def setContraseña(self,Contraseña):
          self.__Contraseña=Contraseña

    def getFunciones(self):
          return self.__Funciones

    def setFunciones(self,Funciones):
          self.__Funciones=Funciones


#el siguiente bloque es un ejemplo por favor no considerar para el codigo final

'''mesero1=Mesero(645641524152,"C.C","ricardo","Arjona","fhujdfhndj@gmail.com","ejduy485","Agregar_servicio Consultar_servicio Actualizar_servicio Eliminar_servicio")
print("el mesero: ",mesero1.getNombres(),mesero1.getApellidos())
print("que tiene: ",mesero1.getTipo_doc())
print("con el numero: ",mesero1.getNum_doc())
print("cuyas funciones son : ",mesero1.getFunciones())'''