class Familia:
    
    def __init__(self):
        self.__lista_familia = []
        
    def agregar_persona(self,persona):
        self.__lista_familia.append(persona)
        
    def imprimir_familia(self):
        print("Familia")
        print("_______________________________________________")
        for i in self.__lista_familia:
            i.imprimir()
        print("_______________________________________________")
        