class Familia:
    
    def __init__(self):
        self.__lista_familia = []
        
    def agregar_persona(self,persona):
        self.__lista_familia.append(persona)
        
    def cantidad_integrantes(self):
        return len(self.__lista_familia)
    
    def cantidad_trabajadores(self):
        total_trabajo = 0
        for per in self.__lista_familia:
            if per.get_trabajo() == "Si":
                total_trabajo =total_trabajo + 1
        return total_trabajo
    
    def promedio(self):
        total = 0
        for num in self.__lista_familia:
            total+= num.get_edad()
        return total/len(self.__lista_familia)   
        
    def imprimir_familia(self):
        print("Familia")
        print("_______________________________________________")
        for i in self.__lista_familia:
            i.imprimir()
        print("_______________________________________________")
        