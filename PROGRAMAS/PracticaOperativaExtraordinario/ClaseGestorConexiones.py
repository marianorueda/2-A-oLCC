import numpy as np
import csv
from ClaseConexion import Conexion

class GestorDeConexiones:
    __arreglo: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int
    def __init__(self):
        self.__incremento=5
        self.__dimension=16
        self.__cantidad=0
        self.__arreglo = np.empty(self.__dimension, dtype=Conexion)
        archivo = open("conexiones.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if fila[0] != "idjugador":
                if self.__cantidad==self.__dimension:
                    self.__dimension+=self.__incremento
                    self.__arreglo.resize(self.__dimension)
                id = int(fila[0])
                direccionIP = fila[1]
                nombreJuego = fila[2]
                fecha = fila[3]
                horaInicio = int(fila[4])
                horaFin = int(fila[5])
                conexion = Conexion(id, direccionIP, nombreJuego, fecha, horaInicio, horaFin)
                self.__arreglo[self.__cantidad]=conexion
                self.__cantidad+=1
        archivo.close()