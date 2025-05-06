import abc
from abc import ABC

class Equipos(ABC):
    __marca : str
    __modelo : str
    __anoFab : int
    __tipoCombustible : str
    __potencia : float
    __capCarga : float
    __tarifa : float
    __cDias : int
    def __init__(self, marca, modelo, anoFab, tipoCombustible, potencia, capCarga, tarifa, cDias):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFab = anoFab
        self.__tipoCombustible = tipoCombustible
        self.__potencia = potencia
        self.__capCarga = capCarga
        self.__tarifa = tarifa
        self.__cDias = cDias

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnoFab(self):
        return self.__anoFab

    def getTipoCombustible(self):
        return self.__tipoCombustible

    def getPotencia(self):
        return self.__potencia

    def getCapCarga(self):
        return self.__capCarga

    def getTarifa(self):
        return self.__tarifa

    def getCDias(self):
        return self.__cDias
    
    @abc.abstractmethod
    def calcularAlquiler(self):
        pass
    
