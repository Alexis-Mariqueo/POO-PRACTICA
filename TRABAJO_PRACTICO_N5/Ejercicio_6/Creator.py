from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):

# -> anotation, permite indicar que es lo que se devuelve, pero no obliga.
    @abstractmethod
    def factory_method(self):
        pass

    def get_notificar(self) -> str:
        
        result = f"Creator: notifico al usuario con: {notificador.notificar_usuario()}"

        return result
