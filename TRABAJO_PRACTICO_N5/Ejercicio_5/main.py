from ConcreteBuilderTorta import ConcreteBuilderTorta
from Director import Director

director = Director()
builder = ConcreteBuilderTorta()
director.builder = builder

print("Torta basico: ")
director.torta_basic()
builder.torta.imprimir_torta()

print("\n")

print("Torta medium: ")
director.torta_medium()
builder.torta.imprimir_torta()

print("\n")

print("Tora Full: ")
director.torta_full()
builder.torta.imprimir_torta()