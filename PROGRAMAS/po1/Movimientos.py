import numpy as np
import csv

class Movimiento:
    __numCuenta: int
    __fecha: str
    __desc:str
    __tipo: str
    __importe: float
    def __init__(self,numCuenta, fecha, desc, tipo, importe):
        self.__numCuenta=numCuenta
        self.__fecha=fecha
        self.__desc=desc
        self.__tipo=tipo
        self.__importe=importe
    def ObtenerNumCuenta(self):
        return self.__numCuenta
    def ObtenerFecha(self):
        return self.__fecha
    def ObtenerDesc(self):
        return self.__desc
    def ObtenerTipo(self):
        return self.__tipo
    def ObtenerImporte(self):
        return self.__importe
    def __lt__(self, otro):
        return self.__numCuenta < otro.ObtenerNumCuenta()

class GestorMovimientos:
    __arreglo: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    def __init__(self):
        self.__incremento=10
        self.__dimension=21
        self.__cantidad=0
        self.__arreglo = np.empty(self.__dimension, dtype=Movimiento)
        archivo = open("MovimientosAbril2024.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__arreglo.resize(self.__dimension)
            numCuenta = fila[0]
            fecha = fila[1]
            desc = fila[2]
            tipo = fila[3]
            importe = fila[4]
            movimiento = Movimiento(numCuenta, fecha, desc, tipo, importe)
            self.__arreglo[self.__cantidad]=movimiento
            self.__cantidad+=1
        archivo.close()

    def ObtenerCantidad(self):
        return self.__cantidad
    
    def Mostrar(self):
        for i in range(20):
            print(self.__arreglo[i].ObtenerNumCuenta())
    
    def ConsultarMovimientos(self, numCuenta):
        j = 0
        band = -1
        while (j<self.__cantidad)and(band == -1):
            if int(numCuenta) == int(self.__arreglo[j].ObtenerNumCuenta()):
                band=1
            else:
                j+=1
        return band

    def CalcularMovimientos(self, numCuenta):
        diferencia=0
        float(diferencia)
        j=0
        for j in range(self.__cantidad):
            if int(self.__arreglo[j].ObtenerNumCuenta()) == int(numCuenta):
                print(f"{self.__arreglo[j].ObtenerFecha()}          {self.__arreglo[j].ObtenerDesc()}          {self.__arreglo[j].ObtenerImporte()}          {self.__arreglo[j].ObtenerTipo()}")
                if self.__arreglo[j].ObtenerTipo() == "C":
                    diferencia += float(self.__arreglo[j].ObtenerImporte())
                else:
                    diferencia -= float(self.__arreglo[j].ObtenerImporte())
        return diferencia
        
    def OrdenarMovimientos(self):
        self.__arreglo.sort()
        print("Los movimientos han sido ordenados")