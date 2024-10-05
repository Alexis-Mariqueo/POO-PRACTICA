class Impuesto:
    
    def __init__(self,nombre,monto,periodo):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado_cobrado = False
        self.__numero_comprobante =  0
    
    def get_nombre(self):
        return self.__nombre
    
    def get_monto(self):
        return self.__monto
    
    def validar_pago(self, mes, numero_comprobante):
        if mes == self.__periodo:
            self.__estado_cobrado = True
            self.__numero_comprobante = numero_comprobante