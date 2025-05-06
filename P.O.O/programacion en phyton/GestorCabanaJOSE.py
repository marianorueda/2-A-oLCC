import csv
import numpy as np
from ModuloCabanaJOSE import Cabana


class gestorcabana:
    __gestorCabana = np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int

    def Agregar(self, cabana):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__gestorCabana.resize(self.__dimension)
        self.__gestorCabana[self.__cantidad] = cabana
        self.__cantidad += 1

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 6
        self.__gestorCabana = np.empty(0, dtype=Cabana)
        archivo = open("Cabañas[1]JOSE.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                numero = int(fila[0])
                canthab = int(fila[1])
                cantcamg = int(fila[2])
                cantcamc = int(fila[3])
                importe = float(fila[4])
                cabana = Cabana(
                    numero, canthab, cantcamg, cantcamc, importe)
                self.Agregar(cabana)
        archivo.close()

    def Mostrar(self, cant, gestorreserva):
        i=0
        for i in range(len(self.__gestorCabana)):
            if(self.__gestorCabana[i]>=cant)and(gestorreserva.BuscarNumCabana(self.__gestorCabana[i].getnumero())==True):
                    print(f"La cabaña numero {self.__gestorCabana[i].getnumero()} esta disponible para el numero de huespedes ingresado")
