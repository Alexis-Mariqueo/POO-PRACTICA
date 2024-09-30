from Personaje import Personaje

class Caballero(Personaje):
    
    def __init__(self,nombre):
        super().__init__(nombre,vida = 100, nivel_ataque = 70, nivel_defensa = 10)