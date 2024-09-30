class Empresa:
    
    def __init__(self,nombre = str,direccion= str) -> None:
        self.__nombre = nombre
        self.__direccion = direccion
        self.__lista_empleados = []
        
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_empleados(self):
        return self.__lista_empleados
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_direccion(self,direccion):
        self.__direccion = direccion
        
    def agregar_empleado(self,empleado):
        self.__lista_empleados.append(empleado)
        
    def total_empleados(self):
        return len(self.__lista_empleados)
    
        
    
        