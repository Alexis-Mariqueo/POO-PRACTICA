from Catalogo import Catalogo

class CatalogoMenor(Catalogo):
    
    def catalogo(self, lista):
        for i in lista:
            if i.get_edad() < 13 :
                i.mostrar_pelicula()
        