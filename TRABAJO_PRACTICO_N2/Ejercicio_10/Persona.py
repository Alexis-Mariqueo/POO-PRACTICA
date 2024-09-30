import random
class Persona:
    
    def __init__(self,edad = 1 ,sexo = "",estudio= bool,trabajo = bool):
        self.__edad = edad
        self.__sexo = sexo
        self.__menores(estudio,trabajo)
        
    def get_edad(self):
        return self.__edad
    
    def get_trabajo(self):
        return self.__trabajo
        
    def __menores(self,estudio,trabajo):
        if self.__edad < 16:
            estudio = True
            self.__estudio = estudio
            trabajo = False
            self.__trabajo = trabajo
            self.__agregar_valor()
        else:
            self.__estudio = estudio
            self.__trabajo = trabajo
            self.__agregar_valor()
            
    def __agregar_valor(self):
        if self.__estudio == True:
            self.__estudio = "Si"
        else:
            self.__estudio = "No"
        if self.__trabajo == True:
            self.__trabajo = "Si"
        else:
            self.__trabajo = "No"
     
    def permitido_trabajar(self):
        if self.__edad >= 16:
            print("Tiene permitido trabajar")
        else:
            print("No tiene permitido trabajar")
    
    def permitido_conducir(self):    
        if self.__edad >= 17:
            print("Tiene permitido conducir un vehiculo particular")
        else:
            print("No tiene permitido conducir un vehiculo particular")
            
    def imprimir(self):
        print("_______________________________________________")
        print("Edad: {}".format(self.__edad))
        print("Sexo: {}".format(self.__sexo))
        print("Estudio: {}".format(self.__estudio))
        print("Trabajo: {}".format(self.__trabajo))
        print("_______________________________________________")
        print("Permisos: ")
        self.permitido_trabajar()
        self.permitido_conducir()
        print("_______________________________________________")
        