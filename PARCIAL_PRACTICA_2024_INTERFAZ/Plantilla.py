class Plantilla:
    
    def __init__(self,usuario,pais_favorito,equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito = equipo_favorito 
        self.__lista_plantel = []
        
    def agregar_carta(self,carta):
        self.__lista_plantel.append(carta)
        
    def quimica_total(self):
        total = 0
        for carta in self.__lista_plantel:
            total+=carta.calcular_quimica(self.__pais_favorito,self.__equipo_favorito)
            
        return total /len(self.__lista_plantel)
    
    def imprimir_plantel(self):
        print("________________________________________________")
        print("Propietario:{}".format(self.__usuario))
        print("Pais favorito:{}".format(self.__pais_favorito))
        print("Equipo favorito:".format(self.__equipo_favorito))
        print("________________________________________________")
        print("Plantel:")
        for carta in self.__lista_plantel:
            print("________________________________________________")
            carta.imprimir()
            print("________________________________________________")
        print("Quimica Total:{}".format(self.quimica_total()))
        print("________________________________________________")