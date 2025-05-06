class vehiculo:
    __marca : str
    __modelo : str
    __anoFab: int
    __capacidad : int 
    __numPlazas : int
    __distancia : float
    __tarifaBase : float
    def __init__(self, marca, modelo, anoFab, capacidad, numPlazas, distancia, tarifa):
        self.__marca = marca
        self.__modelo = modelo
        self.__anoFab = anoFab
        self.__capacidad = capacidad
        self.__numPlazas = numPlazas
        self.__distancia = distancia
        self.__tarifaBase = tarifa
    def getModelo(self):
        return self.__modelo
    def getAnoFab(self):
        return self.__anoFab
    def getCapacidad(self):
        return self.__capacidad
    def getTarifaBase(self):
        return self.__tarifaBase
    def CalcularTarifa(self):
        pass