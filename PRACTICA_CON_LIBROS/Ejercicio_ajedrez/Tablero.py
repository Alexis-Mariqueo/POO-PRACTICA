
class Tablero:
    
    def __init__(self):
        self.__fila = 8
        self.__columna = ["a","b","c","d","e","f","g","h"]
        self.__tiempo = 0.0
        self.__jaque = False
        
    def set_jaque(self):    
        self.__jaque = True
    
    def get_jaque(self):
        return self.__jaque
    
    def get_tiempo(self):
        return self.__tiempo
    
    def tiempo(self):
        if self.__tiempo > 0.60:
            self.__tiempo = self.__tiempo - 0.60
            return self.__tiempo + 1.0
        else:
            return self.__tiempo + 0.1
        