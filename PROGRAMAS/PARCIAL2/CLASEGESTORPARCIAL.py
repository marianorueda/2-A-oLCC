import csv
from CLASEAUTOBUSES import autobus
from CLASEVANES import van

class gestor:
    __lista : list
    def __init__(self):
        self.__lista = []
    def CargaVehiculos(self):
        archivo = open("vehiculos.csv", "r")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if (fila[0] == "A"):
                nAutobus = autobus(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8], fila[9])
                self.__lista.append(nAutobus)
            elif (fila[0] == "V"):
                nVan = van(fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]), float(fila[6]), float(fila[7]), fila[8])
                self.__lista.append(nVan)
        archivo.close
    def BuscarVehiculo(self):
        pos = int(input("Ingrese la posicion del vehiculo en la lista \n"))
        if (pos <= len(self.__lista))and(pos>=0):
            vehiculo = self.__lista[pos]
            if isinstance(vehiculo, autobus):
                print(f"El vehiculo almacenado en la posición -{pos}-, es un Autobus")
            if isinstance(vehiculo, van):
                print(f"El vehiculo almacenado en la posición -{pos}-, es una Van")
    def ContarAyV(self):
        cv = 0
        ca = 0
        i = 0
        for i in range(len(self.__lista)):
            vehiculo = self.__lista[i]
            if isinstance(vehiculo, autobus):
                ca += 1
            if isinstance(vehiculo, van):
                cv += 1
        print(f"Hay -{ca}- Autobuses y -{cv}- Vanes")

    def MostrarVehiculos(self):
        i = 0
        print("Los vehículos son: \n")
        for i in range(len(self.__lista)):
            print(f"Modelo: {self.__lista[i].getModelo()}, Año de fabricación: {self.__lista[i].getAnoFab()}, Capacidad de pasajeros: {self.__lista[i].getCapacidad()}, Tarifa del servicio: {round(self.__lista[i].CalcularTarifa(), 3)}")



            
