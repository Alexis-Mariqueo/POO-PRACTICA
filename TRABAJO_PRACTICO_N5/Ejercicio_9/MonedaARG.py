from DecoratorMonedaArg import DecoratorMonedaArg

class MonedaARG(DecoratorMonedaArg):
   
    def get_line_description(self):
        return self._producto_decorado.get_line_description() + "ARG"    
    
    def get_precio(self):
        return self._producto_decorado.get_precio()
    
   