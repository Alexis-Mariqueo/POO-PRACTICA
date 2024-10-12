
class GestorEnvios:
    
    def __init__(self): ##Como el constructor no especifica que debe tener no coloco atributos
        pass           
    
    #Utilizo este imprimir para no repetir codigo, segun el tipo imprime uno o el otro
    def __imprimir(self,transporte,paquete,distancia): ## declaro este metodo privado para implementarlo en el metodo gestionar envio
        if transporte.get_tipo() == "Furgoneta":
            print("Gestionando el paquete Grande:")
            print("Paquete demasiado pesado para el cartero")
            print(f"La furgoneta tarda {transporte.get_tiempo()} con un costo de {transporte.get_costo()}$,indicador de costo transporte {transporte.transportar_paquetes(paquete.get_peso(),distancia)}")
            print(f"Mejor indicador costo{transporte.transportar_paquetes(paquete.get_peso(),distancia)}")
            print(paquete) ##Muestro los valores del paquete
        if transporte.get_tipo() == "Cartero":
            print("Gestionando el paquete liviano:")
            print("Paquete demasiado liviano para la furgoneta")
            print(f"El cartero tarda {transporte.get_tiempo()} con un costo de {transporte.get_costo()}$,indicador de costo transporte {transporte.transportar_paquetes(paquete.get_peso(),distancia)}")
            print(f"Mejor indicador costo {transporte.transportar_paquetes(paquete.get_peso(),distancia)}")
            print(paquete) ##Muestro los valores del paquete
            
    ##Coloco el metodo en esta clase      
    def gestionar_envio(self,lista_transporte,paquete,distancia): ##Como especifica que deba estar este metodo solo en la clase Gestor Envio
        for i in lista_transporte:                       ##RECORRO LA LISTA DE TRANSPORTE
            if paquete.calcular_peso_volumetrico() <= 100.0 :
                self.__imprimir(i,paquete,distancia)    
            if paquete.calcular_peso_volumetrico() <= 5.0:
                self.__imprimir(i,paquete,distancia)
            if paquete.calcular_peso_volumetrico() > 100.0:
                print("No hay transporte disponible para este tipo de paquete")                
    
                  
                                                                   
    
        