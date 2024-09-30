from Alumno import Alumno

alumno1 = Alumno()
alumno1.set_nombre("Alejandro")
alumno1.set_apellido("Rojas")
alumno1.set_dni(11111111)

alumno2 = Alumno().iniciar_con_nombre_ape("Martin","Rosales")
alumno2.set_dni(11111112)

print(f"{alumno1.get_nombre()}, {alumno1.get_apellido()}- DNI:{alumno1.get_dni()}")
print(f"{alumno2.get_nombre()}, {alumno2.get_apellido()}- DNI:{alumno2.get_dni()}")