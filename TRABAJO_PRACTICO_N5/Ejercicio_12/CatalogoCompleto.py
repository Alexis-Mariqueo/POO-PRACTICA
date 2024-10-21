from Catalogo import Catalogo

class CatalogoCompleto(Catalogo):
    
    def catalogo(self, lista):
        for i in lista:
            i.mostrar_pelicula()