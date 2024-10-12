from abc import ABC,abstractmethod ##Esto debe estar porque se debe implementar todas las clases que las usen

class Transporte(ABC): ##Creo una interfaz formal
    
    @abstractmethod    ##Considero que debe estar en todos los metodos que la implementencion
    def get_tipo(self): 
        pass
    
    @abstractmethod ##Conseidero que debe tener esto
    def get_tiempo(self):
        pass
    
    @abstractmethod ##Conseidero que debe tener esto
    def get_costo(self):
        pass
    
    @abstractmethod    
    def transportar_paquetes(self,distancia,peso_paquete): 
        pass