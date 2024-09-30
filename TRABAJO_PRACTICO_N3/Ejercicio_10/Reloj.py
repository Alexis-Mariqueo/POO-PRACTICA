import random
class Reloj:
    
    def __init__(self,personal):
        self.__personal = personal
        self.__mes = random.randrange(1,12)
        self.__minimo_requerido = random.randrange(44,130)
        
    def mostrar_informe(self):
        if self.__personal.asignacion_horas() > self.__minimo_requerido:
            self.__cumple = True
        else:
            self.__cumple = False
        self.__personal.imprimir()
        print("Horas Trabajadas: {}".format(self.__personal.asignacion_horas()))
        print("Mes: {}".format(self.__mes))
        if self.__cumple  == True:
            self.__cumple = "Si Cumple"
            print("Cumplimiento de minimo de horas trabajadas: {}".format(self.__cumple))
        else:
            self.__cumple = "No Cumple"
            print("Cumplimiento de mininimo de horas trabajadas: {}".format(self.__cumple))
            
        