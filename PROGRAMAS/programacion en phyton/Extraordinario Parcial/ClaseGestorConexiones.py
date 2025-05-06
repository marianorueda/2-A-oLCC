import numpy as np
from ClaseConexion import Conexion
import csv
class GestorConexiones:
    __arreglo: np.ndarray
    __dimension: int
    __incremento: int
    __cantidad: int 
    def __init__(self):
        self.__incremento=5
        self.__dimension=15
        self.__cantidad=0
        self.__arreglo = np.empty(self.__dimension, dtype=Conexion)
        archivo = open("Conexiones.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__arreglo.resize(self.__dimension)
            id = int(fila[0])
            direccionIp = fila[1]
            nombreJuego = fila[2]
            fecha = fila[3]
            horaIni = int(fila[4])
            horaFin = int(fila[5])
            conexion = Conexion(id, direccionIp, nombreJuego, fecha, horaIni, horaFin)
            self.__arreglo[self.__cantidad]=conexion
            self.__cantidad+=1
    def MostrarConexiones(self, id):
        print("Ip de conexion    Juego         Fecha         Hora deInicio       Hora de Finalizacion")
        for i in range (self.__cantidad):
            if id == self.__arreglo[i].getId():
                print(f"{self.__arreglo[i].getDireccionIp()}       {self.__arreglo[i].getNombreJuego()}       {self.__arreglo[i].getFecha()}       {self.__arreglo[i].getHoraIni()}       {self.__arreglo[i].getHoraFin()}")
    def ConexionesJuego(self, juego, ContenedorGammer):
        for i in range (self.__cantidad):
            if juego == self.__arreglo[i].getNombreJuego():
                print(f"Conexiones para el juego {juego}")
                aux = self.__arreglo[i].getId()
                ContenedorGammer.MostrarGammers(aux)