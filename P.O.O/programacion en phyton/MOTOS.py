class Moto:
    __patente : int
    __marca : str
    __NyA : str
    __Km : float
    def __init__(self, patente, marca, NyA, Km):
        self.__patente = int(patente)
        self.__marca = marca
        self.__NyA = NyA
        self.__Km = float(Km)
    def 