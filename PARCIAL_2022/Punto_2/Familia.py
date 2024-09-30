class Familia:
    
    def __init__(self,apellido_familia):
        self.__apellido_familia = apellido_familia
        self.__lista_personas = []
        
    def agregar_familiar(self,persona):
        self.__lista_personas.append(persona)    

    def promedio_edad(self):
        total = 0
        for i in self.__lista_personas:
            total += i.get_edad()
        promedio = total/len(self.__lista_personas)
        return promedio
            
    def mostrar_integrante(self):
        print("Familia {}".format(self.__apellido_familia))
        print("Promedio de edad: {}".format(self.promedio_edad()))
        for per in self.__lista_personas:
            per.imprimir()