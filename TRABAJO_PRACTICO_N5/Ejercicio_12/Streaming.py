class Streaming:
    
    def __init__(self):
        self.__estrategia_catalogo = None
        
    def set_estrategia_catalogo(self,catalogo):
        self.__estrategia_catalogo = catalogo
        
    def catalogo(self,lista):
        if self.__estrategia_catalogo  is not None:
            self.__estrategia_catalogo.catalogo(lista)
        else:
            print("No ha seleccionado ningun catalogo")