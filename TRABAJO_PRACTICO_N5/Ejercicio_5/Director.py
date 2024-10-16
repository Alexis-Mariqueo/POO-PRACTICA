
class Director:
    
    def __init__(self, constructor_de_torta):
        self.__constructor_de_torta = constructor_de_torta

    def torta_vainilla(self):
        self.__constructor_de_torta.crear_torta()
        self.__constructor_de_torta.agregar_masa("Vainilla")
        self.__constructor_de_torta.agregar_relleno("Dulce de Leche con Banana")

    def torta_coco(self):
        self.__constructor_de_torta.crear_torta()
        self.__constructor_de_torta.agregar_masa("Coco")
        self.__constructor_de_torta.agregar_relleno("Merengue")

    def torta_chocolate(self):
        self.__constructor_de_torta.crear_torta()
        self.__constructor_de_torta.agregar_masa("Chocolate")
        self.__constructor_de_torta.agregar_relleno("Crema con Frutilla y Mermelada de Frutos Rojos")

    def get_torta(self):
        return self.__constructor_de_torta.get_torta()
    