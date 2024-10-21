from Estado import Estado
from abc import ABC

class Caja(ABC):
    
    def __init__(self,nombre_cajero):
        self.__nombre_cajero = nombre_cajero


class CajaAbierta(Estado,Caja):
    
    def __init__(self):
        super().__init__('Alexis')
    
    def abierta(self,cliente):
        for i in cliente.get_fila():
            i.imprimir_cliente()
        lista=cliente.get_fila()
        lista.clear()
        print("No hay siguiente cliente en la fila")
        cliente.set_estado(CajaCerrada())
        
    def suspendida(self, cliente):
        print("No puede cambiar el estado ha suspendida, debe estar abierta para todo el publico")
    
    def cerrada(self):
        print('La caja ha cerrado')
        
class CajaSuspendida(Estado,Caja):
    
    def __init__(self):
        super().__init__('Alexis')
    
    def abierta(self, cliente):
        print("la caja ha abierto pero debe estar para personas con prioridad")
    
    def suspendida(self,cliente):
        for i in cliente.get_fila():
            if i.get_edad() >= 60:
                i.imprimir_cliente()
            else:
                print("No se admiten personas menores de 60 años en esta caja")
        lista = cliente.get_fila()
        lista.clear()
        cliente.set_estado(CajaCerrada())
    
    def cerrada(self,cliente):
        print('La caja ha cerrado')
    
class CajaCerrada(Estado,Caja):
    
    def __init__(self):
        super().__init__('Alexis')
    
    def abierta(self, cliente):
        print("Esta caja no puede abrir porque esta cerrada")
    
    def suspendida(self, cliente):
        print("Esta caja no puede estar suspendida, debe estar cerrada")
    
    def cerrada(self,cliente):
        print("No se atienden clientes en esta hora")