class Producto:
    
    def __init__(self,nombre,dosis,precio):
        self.__nombre = nombre
        self.__dosis = dosis
        self.__precio = precio
        
    def get_precio(self):
        return self.__precio
    
    def imprimir(self):
        print("{}    {}mg        ${}".format(self.__nombre,self.__dosis,self.__precio))
        