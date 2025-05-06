from ClaseSolicitante import Solicitante
from random import uniform
import numpy as np

class ColaSecuencial:
    __ult : int
    __pri : int
    __cont : int
    __arreglo : np.ndarray

    def __init__(self):
        self.__pri = 0
        self.__ult = 0
        self.__cont = 0
        self.__arreglo = np.empty(5,dtype = Solicitante)

    def vacia(self):
        return self.__cont == 0
    
    def llena(self):
        return self.__cont == len(self.__arreglo)
    
    def insertar(self,item):
        if not self.llena():
            self.__arreglo[self.__ult] = item
            self.__ult = (self.__ult +1) % len(self.__arreglo)
            self.__cont += 1
        else:
            print("No hay espacio en la cola")

    def suprimir(self):
        elemento = None
        if not self.vacia:
            elemento = self.__arreglo[self.__pri]
            self.__pri = (self.__pri + 1) % len(self.__arreglo)
        else:
            print("La cola esta vacia")
        return elemento

    def llegaCliente(self):
        band = False
        random = uniform(0,1)
        if random <= 1/10:
            band = True
        return band

    def calcularTiempoEspera(self):
        sum = 0
        for i in range (self.__pri, self.__cont, 1):
            sum += self.__arreglo[i].getTiempoEspera()
        return sum
    
    def tiempo(self):
        if not self.vacia():
            if self.__arreglo[self.__pri].getTiempoEjec() > 1:
                
