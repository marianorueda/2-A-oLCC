from ClaseGammer import Gammer
class Nodo:
    __gammer: Gammer
    __siguiente: object

    def __init__(self,gammer):
        self.__gammer=gammer
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__gammer

    def getSiguiente(self):
        return self.__siguiente