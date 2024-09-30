class Plantilla:
    
    def __init__(self,usuario,pais_favorito,equipo_favorito):
        self.__usuario = usuario
        self.__pais_favorito = pais_favorito
        self.__equipo_favorito = equipo_favorito
        self.__lista_cartas = []
        
    def agregar_carta(self,carta):
        self.__lista_cartas.append(carta)    
    
    def quimica_total(self):
        total = 0
        for carta in self.__lista_cartas:
            total+= carta.calcular_quimica(self.__pais_favorito,self.__equipo_favorito)
            
        return total/len(self.__lista_cartas) 
        
    def imprimir_plantel(self):
        print("_________________________________________")
        print("Propietario:{}".format(self.__usuario))
        print("Equipo:{}".format(self.__equipo_favorito))
        print("Pais:{}".format(self.__pais_favorito))
        print("_________________________________________")
        for i in self.__lista_cartas:
            print("_________________________________________")
            i.imprimir()
            print("_________________________________________")
            
        print("_________________________________________")
        print("Quimica Total:{}".format(self.quimica_total()))
        print("_________________________________________")
        
        
        