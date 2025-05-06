class Departamento:
    __id : int
    __NyA : str
    __numPiso : int
    __numDepto : int
    __chab : int
    __cbanos : int
    __sup : float
    def __init__(self, id, NyA, numPiso, numDepto, chab, cbanos, sup):
        self.__id = id
        self.__NyA = NyA
        self.__numPiso = numPiso
        self.__numDepto = numDepto
        self.__chab = chab
        self.__cbanos = cbanos
        self.__sup = sup
    def obtenerId(self):
        return self.__id
    def obtenerNyA(self):
        return self.__NyA
    def obtenerNumPiso(self):
        return self.__numPiso
    def obtenerNumDepto(self):
        return self.__numDepto
    def obtenerChab(self):
        return self.__chab
    def obtenerCbanos(self):
        return self.__cbanos
    def obtenerSup(self):
        return self.__sup
    