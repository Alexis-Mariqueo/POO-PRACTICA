import random
class Persona:
    
    def __init__(self,edad = 1 ,sexo = "",estudio= bool,trabajo = bool,puesto = ""):
        self.__edad = edad
        self.__sexo = sexo
        self.__menores(estudio,trabajo)
        self.__puesto = puesto
        
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
        
    def imprimir(self):
        print("_______________________________________________")
        print("Edad: {}".format(self.__edad))
        print("Sexo: {}".format(self.__sexo))
        print("Estudio: {}".format(self.__estudio))
        print("Trabajo: {}".format(self.__trabajo))
        print(self.__puesto)
        print("_______________________________________________")
        