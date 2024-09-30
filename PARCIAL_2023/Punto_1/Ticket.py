import random
class Ticket:
    
    def __init__(self,fecha):
        self.__fecha = fecha
        self.__numero_ticket = random.randrange(1000000,9999999)
        self.__lista_productos = []
    
    def agregar_producto(self,producto):
        self.__lista_productos.append(producto)    
        
    def calcular_total(self):
        total = 0
        for pro in self.__lista_productos:
            total = total + pro.get_precio()        
        return total
    
    def imprimir_producto(self):
        print("Producto     Dosis       Precio")
        for i in self.__lista_productos:
            i.imprimir()
    
    def imprimir_ticket(self):
        print("Fecha: {}".format(self.__fecha))
        print("N° {}".format(self.__numero_ticket))
        self.imprimir_producto()
        print("                         Total        ")
        print("                          ${}".format(self.calcular_total()))
        
    