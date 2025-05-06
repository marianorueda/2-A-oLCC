from CLASEPACIENTE import Paciente

class Nodo:
    __paciente: Paciente
    __siguiente: object

    def __init__(self, paciente):
        self.__paciente = paciente
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getDato(self):
        return self.__paciente

    def getSiguiente(self):
        return self.__siguiente