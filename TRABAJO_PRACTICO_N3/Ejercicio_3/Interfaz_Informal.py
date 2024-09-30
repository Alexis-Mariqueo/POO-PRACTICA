##Una clase con los metodos definidos pero sin cuerpo y con
#subclase que le dan la implementación

class Vehiculo():
    def arrancar(self):
        pass
    def acelerar(self, velocidad):
        pass
    def frenar(self):
        pass
    def apagar(self):
        pass

class Auto(Vehiculo):
    def arrancar(self):
        print("El auto arranca.")

    def acelerar(self, velocidad):
        print(f"El auto acelera a {velocidad} km/h.")

    def frenar(self):
        print("El auto frena.")

    def apagar(self):
        print("El auto se apaga.")


class Moto(Vehiculo):
    def arrancar(self):
        print("La moto arranca.")

    def acelerar(self, velocidad):
        print(f"La moto acelera a {velocidad} km/h.")

    def frenar(self):
        print("La moto frena.")

    def apagar(self):
        print("La moto se apaga.")

vehiculos = [Auto(),Moto()]

for vehiculo in vehiculos:
  vehiculo.arrancar()
  vehiculo.acelerar(60)
  vehiculo.frenar()
  vehiculo.apagar()
  print()