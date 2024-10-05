from Persona import Persona

class Profesor(Persona):
    
    def __init__(self, legajo, nombre, apellido, dni, tipo):
        super().__init__(legajo, nombre, apellido, dni, tipo)
        self.__materias = []
        self.__alumnos = []
    
    def get_alumnos(self):
        return self.__alumnos    
        
    def agregar_materia(self,materia):
        self.__materias.append(materia)
        
    def agregar_alumno(self,alumno):
        self.__alumnos.append(alumno)
        
            
    def mostrar_materia(self):
        print("Materias")
        for i in self.__materias:
            print("_______________________________________")
            print(i)
            print("_______________________________________")            
        for alum in self.get_alumnos():
            print("_______________________________________")            
            alum.mostrar_informacion()
            print("_______________________________________")    
