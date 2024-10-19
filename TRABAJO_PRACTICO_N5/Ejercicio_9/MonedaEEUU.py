from DecoratorMonedaEEUU import DecoratorMonedaEEUU

class MonedaEEUU(DecoratorMonedaEEUU):

    def get_line_description(self):
        return self._producto_decorado.get_line_description() + "$USD"
    
    def get_precio(self):
        return self._producto_decorado.get_precio()