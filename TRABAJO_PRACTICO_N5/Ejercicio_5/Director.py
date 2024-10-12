from TortaBuilder import TortaBuilder

class Director:
    
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> TortaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: TortaBuilder) -> None:
        self._builder = builder

    def torta_basic(self) -> None:
        self.builder.set_masa("Vainilla")
        self.builder.set_relleno("Nutella con frutillas")

    def torta_medium(self) -> None:
        self.builder.set_masa("Coco")
        self.builder.set_relleno("Dulce de leche con banana")

    def torta_full(self)->None:
        self.builder.set_masa("Chocolate")
        self.builder.set_relleno("Mermelada de Frutilla")