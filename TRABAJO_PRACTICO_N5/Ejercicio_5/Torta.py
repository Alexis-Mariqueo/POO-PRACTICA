
class Torta:
    
    def __init__(self):
        self._masa = " "
        self._relleno= " "
        
    def imprimir_torta(self)-> None:
        print(f"Ingredientes de la torta:\nMasa: {''.join(self._masa)}\nRelleno: {''.join(self._relleno)}",end="")
        
        