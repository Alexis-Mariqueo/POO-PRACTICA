
class Tablero:
    
    def __init__(self):
        self.__fila = 8
        self.__columna = ["a","b","c","d","e","f","g","h"]
        self.__tiempo = 0.0
        self.__jaque = False
        
    def jaque(self):    
        self.__jaque = True
        return self.__jaque
    
    def tiempo(self):
        if self.__tiempo > 0.60:
            self.__tiempo = self.__tiempo - 0.60
            return self.__tiempo + 1.0
        else:
            return self.__tiempo + 0.1
        