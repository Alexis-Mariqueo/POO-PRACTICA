from Profesor import Profesor
from Alumno import Alumno
import random

lista_alumnos = []
tipo_cursada = ["Regular","Maestria"]

for i in range(0,10):
    lista_alumnos.append(Alumno(random.randint(1000,9999),f"Nombre_{i}",f"Apellido_{i}",random.randint(10000000,99999999),random.choice(tipo_cursada)))


profesor_1 = Profesor(random.randint(1000,9999),"Gusman","Mendez",random.randint(10000000,99999999),"Titulares")
profesor_1.agregar_materia("POO")
profesor_1.agregar_materia("Base de datos")
profesor_1.agregar_alumno(random.choice(lista_alumnos))
profesor_1.agregar_alumno(random.choice(lista_alumnos))
profesor_1.agregar_alumno(random.choice(lista_alumnos))
profesor_2 = Profesor(random.randint(1000,9999),"Martin","Polo",random.randint(10000000,99999999),"Asociados")
profesor_2.agregar_materia("Algoritmica y Programación")
profesor_2.agregar_alumno(random.choice(lista_alumnos))
profesor_2.agregar_alumno(random.choice(lista_alumnos))
profesor_2.agregar_alumno(random.choice(lista_alumnos))
profesor_3 = Profesor(random.randint(1000,9999),"Vanina","Perez",random.randint(10000000,99999999),"Titulares")
profesor_3.agregar_materia("Sistemas y Organizaciones")
profesor_3.agregar_alumno(random.choice(lista_alumnos))
profesor_3.agregar_alumno(random.choice(lista_alumnos))
profesor_3.agregar_alumno(random.choice(lista_alumnos))

profesor_1.mostrar_materia()
profesor_2.mostrar_materia()
profesor_3.mostrar_materia()