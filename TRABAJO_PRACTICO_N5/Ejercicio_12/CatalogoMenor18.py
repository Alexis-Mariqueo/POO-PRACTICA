from Catalogo import Catalogo

class CatalogoMenor18(Catalogo):
    
    def catalogo(self, lista):
        for i in lista:
            if i.get_edad() < 18:
                i.mostrar_pelicula()