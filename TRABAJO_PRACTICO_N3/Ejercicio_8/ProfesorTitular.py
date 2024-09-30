from Persona import Persona

class ProfesorTitular(Persona):
    
    def __init__(self, nombre, apellido, edad, horas_trabajadas,antiguedad):
        super().__init__(nombre, apellido, edad, horas_trabajadas, valor_hora = 300.00)
        self.__valor_antiguedad = 1000.00
        self.__antiguedad = antiguedad
        
    def set_valor_antiguedad(self,valor_anti): ## por si en algun momento el valor de antiguedad cambia
        self.__valor_antiguedad = valor_anti
        
    def __get_renumeracion_antiguedad(self):
        return self.__valor_antiguedad * self.__antiguedad
    
    def get_renumeracion_mensual(self):
        return (self._valor_hora * self._horas_trabajadas) + self.__get_renumeracion_antiguedad()

    def imprimir(self):
        super().imprimir()
        print("Renumeracion: {}".format(self.get_renumeracion_mensual()))