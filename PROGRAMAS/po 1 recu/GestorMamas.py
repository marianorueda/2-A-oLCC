import numpy as np
import csv
from ModuloMamas import Mama

class gestorMamas:
    __arreglo: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    def __init__(self):
        self.__incremento=5
        self.__dimension=15
        self.__cantidad=0
        self.__arreglo = np.empty(self.__dimension, dtype=Mama)
        archivo = open("Mamas.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__arreglo.resize(self.__dimension)
            dni = int(fila[0])
            edad = fila[1]
            AyN = fila[2]
            mama = Mama(dni, edad, AyN)
            self.__arreglo[self.__cantidad]=mama
            self.__cantidad+=1
        archivo.close()
    def BuscarMama(self, dni, gestorNacimientos):
        i=0
        while (dni != self.__arreglo[i].ObtenerDni())and(i <= self.__cantidad):
            i+=1
        if(i <= self.__cantidad):
            print(f"Apellido y Nombre: {self.__arreglo[i].ObtenerNom()}")
            print(f"Edad: {self.__arreglo[i].ObtenerEdad()}")
            gestorNacimientos.MostrarNacimientos(dni)
    def ObtenerArreglo(self):
        return self.__arreglo
    def BuscarPartosMultiples(self, gestorNacimientos):
        j=0
        print("Los datos de las mamas con partos múltiples son:")
        for j in range (self.__cantidad):
            c1 = gestorNacimientos.PartosMultiples(self.__arreglo[j].ObtenerDni())
            if (c1 > 1):
                print(f"DNI: {self.__arreglo[j].ObtenerDni()}       Apellido y Nombre: {self.__arreglo[j].ObtenerNom()}       Edad: {self.__arreglo[j].ObtenerEdad()}")