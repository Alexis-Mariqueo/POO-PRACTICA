from abc import ABC, abstractmethod

class Precio(ABC):
    
    @abstractmethod
    def get_precio(self):
        pass
    
    @abstractmethod
    def get_line_description(self):
        pass
    
    