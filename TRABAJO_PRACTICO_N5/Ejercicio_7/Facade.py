from __future__ import annotations
from Helper import Helper
from CaseHelper import CaseHelper

# El patrón Facade proporciona un práctico acceso a una parte 
# específica de la funcionalidad del subsistema. 
# Sabe a dónde dirigir la petición del cliente y cómo operar 
# todas las partes móviles.
class Facade:
    
    def __init__(self,helper_1,helper_2) -> None:
        self.__helper_1 = Helper() or helper_1
        self.__helper_2 = CaseHelper() or helper_2

    def operation(self,palabra) -> str:
        results = []
        results.append(f"Palabra: {palabra}")
        results.append("Traduccion de palabra:")
        results.append(self.__helper_1.translate_to_english(palabra))
        results.append("Convierte la palabra en mayuscula:")
        results.append(self.__helper_2.to_uppercase(palabra))
        results.append("Convierte la palabra en minuscula:")
        results.append(self.__helper_2.to_lowercase(palabra))
        return "\n".join(results)
