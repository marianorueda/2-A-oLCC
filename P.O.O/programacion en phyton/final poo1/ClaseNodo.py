from ClaseClienteLocal import ClienteLocal

class Nodo:
    __cliente: ClienteLocal
    __siguiente: object

    def __init__(self, clienteLocal):
        self.__cliente=clienteLocal
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__cliente

    def getSiguiente(self):
        return self.__siguiente