from CLASEPLANES import plan
class Nodo:
    __plan: plan
    __siguiente: object

    def __init__(self,Plan):
        self.__plan=Plan
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__plan

    def getSiguiente(self):
        return self.__siguiente