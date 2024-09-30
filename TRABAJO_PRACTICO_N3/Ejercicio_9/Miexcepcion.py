class Miexcepcion(Exception):
    
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje

        
    def metodo(self,sms,llamada,gb):
        if sms < 0.0 :
            raise Miexcepcion("El total de mesajes ingresado debe ser positivo")
        if llamada < 0.0:
            raise Miexcepcion("El total de llamadas ingresado debe ser positivo")
        if gb < 0.0:
            raise Miexcepcion("El total de consumo de GB ingresado debe ser positivo")
    