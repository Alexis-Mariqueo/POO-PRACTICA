from Precio import Precio 

class Producto(Precio):
    
    def __init__(self,precio):
        self.__precio = precio

    def get_line_description(self)->str:
        return '$'  

    def get_precio(self):
        return  self.__precio 
    


