from Persona import Persona
import datetime

persona_1 = Persona("Alexis","Mariqueo",datetime.date(2003,6,17))
persona_2 = Persona("Marta","Nuñez",datetime.date(1985,7,6))
persona_3 = Persona("Enzo","Puñalef",datetime.date(2008,10,1))

persona_1.calcular_edad()
persona_2.calcular_edad()
persona_3.calcular_edad()
print(persona_1)
print(persona_2)
print(persona_3)