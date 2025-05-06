from CLASEEQUIPOS import Equipos

class Nodo:
    __equipo: Equipos
    __siguiente: object

    def __init__(self, equipo):
        self.__equipo = equipo
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente =siguiente

    def getDato(self):
        return self.__equipo

    def getSiguiente(self):
        return self.__siguiente