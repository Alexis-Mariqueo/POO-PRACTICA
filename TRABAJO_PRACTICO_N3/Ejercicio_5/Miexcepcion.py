
class Miexcepcion(Exception):
    
    def __init__(self,mensaje) -> None:
        self.mensaje = mensaje
    
    def metodo(self,vida,nombre):
        if vida < 0:
            vida = 0
            raise Miexcepcion(f"El personaje {nombre} ha muerto por su bajo nivel de vida.")