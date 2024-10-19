from Precio import Precio

class DecoratorMonedaEEUU(Precio):
    
    def __init__(self,producto_decorado):
        self._producto_decorado = producto_decorado
        
    def get_precio(self):
        return self._producto_decorado.get_precio() 
    
    def get_line_description(self):
        return self._producto_decorado.get_line_description()
        

    
