from Archivo import Archivo
from Carpeta import Carpeta

carpeta_1 = Carpeta('Carpeta_1')
carpeta_1.asignar_rol('Carpeta de Archivos')
carpeta_2 = Carpeta('Carpeta_2')
carpeta_2.asignar_rol('Carpeta de Archivos')
carpeta_3 = Carpeta('Carpeta_3')
carpeta_3.asignar_rol('Carpeta de Archivos')

archivo_1 = Archivo('Archivo_1')
archivo_1.asignar_rol('txt')
archivo_2 = Archivo ('Archivo_2')
archivo_2.asignar_rol('py')
archivo_3 = Archivo ('Archivo_3')
archivo_3.asignar_rol('png')
archivo_4 = Archivo('Archivo_4')
archivo_4.asignar_rol('txt')

carpeta_1.agregar_elemento(carpeta_2)
carpeta_2.agregar_elemento(archivo_1)
carpeta_2.agregar_elemento(archivo_2)
carpeta_1.agregar_elemento(archivo_3)
carpeta_3.agregar_elemento(archivo_4)

carpeta_1.mostrar_contenido()
carpeta_3.mostrar_contenido()