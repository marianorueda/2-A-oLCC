class Solicitante:
    __tiempoEjec : int
    __tiempoEspera : int

    def __init__(self):
        self.__tiempoEjec = 15
        self.__tiempoEspera = 0

    def getTiempoEspera(self):
        return self.__tiempoEspera
    
    def setTiempoEspera(self, sum):
        self.__tiempoEspera = sum

    def getTiempoEjec(self):
        return self.__tiempoEjec