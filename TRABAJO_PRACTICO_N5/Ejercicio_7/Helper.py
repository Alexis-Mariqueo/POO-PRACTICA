
##El Subsistema Complejo consiste en decenas de objetos diversos. 
# Para lograr que todos hagan algo significativo, debes profundizar 
# en los detalles de implementación del subsistema, que pueden 
# incluir inicializar objetos en el orden correcto y suministrarles
# datos en el formato adecuado.
##
##
##Las clases del subsistema no conocen la existencia de la fachada. 
# Operan dentro del sistema y trabajan entre sí directamente.
#####

class Helper:
    def __init__(self):
        # Diccionario de traducciones 
        self.translations = {
            "hola": "hello",
            "mundo": "world",
            "perro": "dog",
            "gato": "cat",
            "casa": "house"
        }

    def translate_to_english(self, word): ##Si la palabra no se encuentra en el diccionario
        return self.translations.get(word.lower(), "Translation not found")
