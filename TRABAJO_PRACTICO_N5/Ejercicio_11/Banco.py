from Caja import CajaSuspendida

class Banco:
    
    def __init__(self):
        self.__caja_estado_actual = CajaSuspendida()
        self.__cliente = []
        
    def set_estado(self,nuevo_estado):
        self.__caja_estado_actual = nuevo_estado
    
    def get_fila(self):
        return self.__cliente    
    
    def agregar_persona(self,persona):
        self.__cliente.append(persona)
        
    def eliminar_persona(self,persona):
        self.__cliente.remove(persona)
        
    def abierta(self):
        self.__caja_estado_actual.abierta(self)
        
    def suspendida(self):
        self.__caja_estado_actual.suspendida(self)
        
    def cerrada(self):
        self.__caja_estado_actual.cerrada(self)
        
    
        