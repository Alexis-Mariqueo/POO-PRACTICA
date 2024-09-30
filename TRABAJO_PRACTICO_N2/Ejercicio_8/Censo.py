class Censo:
    
    def __init__(self,fecha_censo = 0):
        self.__fecha_censo = fecha_censo
        self.__familias_censadas = []
        
    def agregar_familia(self,familia):
        self.__familias_censadas.append(familia)
        
    def mostrar_censo(self):
        print("Fecha Censo: {}".format(self.__fecha_censo))
        print("Personas Censadas")
        for num in self.__familias_censadas:
            num.imprimir_familia()