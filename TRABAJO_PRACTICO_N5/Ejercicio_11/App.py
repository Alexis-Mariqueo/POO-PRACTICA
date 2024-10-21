from Cliente import Cliente
from Banco import Banco

banco = Banco()
persona_1=Cliente('Alex',22)
banco.agregar_persona(Cliente('Daniela',20))
banco.agregar_persona(Cliente('Marcos',22))
banco.agregar_persona(Cliente('Dante',70))


banco.abierta()
print()
banco.suspendida()
print()
banco.cerrada()