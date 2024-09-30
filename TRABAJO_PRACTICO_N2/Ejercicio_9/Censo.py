class Censo:
    
    def __init__(self,fecha_censo = 0):
        self.__fecha_censo = fecha_censo
        self.__familias_censadas = []
        
    def agregar_familia(self,familia):
        self.__familias_censadas.append(familia)
        
    def total_familias_censadas(self):
        return len(self.__familias_censadas)
    
    def total_personas(self):
        total = 0
        for i in self.__familias_censadas:
            total += i.cantidad_integrantes()
        return total
    
    def total_trabajadores(self):
        total_trabaja = 0
        for per in self.__familias_censadas:
            total_trabaja += per.cantidad_trabajadores()
        return total_trabaja
    
    def promedio_edad (self):
        print("Promedio de edad por familia")
        for i in self.__familias_censadas:
            print(f"Promedio edad: {i.promedio()}")
        
    def mostrar_personas_censadas(self):
        print("Fecha Censo: {}".format(self.__fecha_censo))
        print("Personas Censadas")
        for num in self.__familias_censadas:
            num.imprimir_familia()
            
    def mostrar_datos_censo(self):
        print("Fecha Censo: {}".format(self.__fecha_censo))
        print("Datos Censo")
        print("Total Familias Censadas: {}".format(self.total_familias_censadas()))
        print("Total Personas: {}".format(self.total_personas()))
        self.promedio_edad()
        print("Total de personas que trabajan: {}".format(self.total_trabajadores()))