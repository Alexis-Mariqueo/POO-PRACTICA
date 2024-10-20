

class SistemaMetereologico():
    
    def __init__(self,estado_clima):
        self.__estado_clima= estado_clima
        self.__observadores = []

    def agregar_observador(self, observador):
        self.__observadores.append(observador)

    def eliminar_observador(self, observador):
        self.__observadores.remove(observador)

    def __notificar_actualizacion(self):
        for obser in self.__observadores:
            obser.actualizar(self.__estado_clima)
        
    def set_clima(self,nuevo_estado_clima):
        self.__estado_clima = nuevo_estado_clima
        self.__notificar_actualizacion()
        
    def get_clima(self):
        return self.__estado_clima