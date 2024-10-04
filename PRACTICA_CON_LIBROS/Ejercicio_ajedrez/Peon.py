from Pieza import Pieza

class Peon(Pieza):
    
    def __init__(self):
        super().__init__(tipo_pieza = "Peon")
        
    def mover_pieza(self, movimiento, fila, columna):
        super().mover_pieza(movimiento, fila, columna)
        if movimiento == 1:
            print(f"La pieza se movio 1 paso")
        if movimiento == 2:
            print(f"La pieza se movio 2 pasos")
            