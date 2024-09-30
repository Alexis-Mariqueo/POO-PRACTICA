from abc import ABC

class Personaje(ABC):
    
    def __init__(self,nombre,vida,nivel_ataque,nivel_defensa):
        self._nombre = nombre
        self._vida = vida
        self._nivel_ataque = nivel_ataque
        self._nivel_defensa = nivel_defensa
        
    def set_vida(self,vida):
        self._vida = vida
        
    def get_vida(self):
        return self._vida
    
    def get_nombre(self):
        return self._nombre
        
    def atacar(self):
        return self._nivel_ataque
    
    
    def defender(self,daño): # los dos se defienden de la misma forma
        daño = self._nivel_ataque - daño
        if daño < 0:
            daño = daño * -1
            self._vida -=  daño
            return self._vida
        else:
            self._vida  -= daño
            return self._vida
        
            
        
        