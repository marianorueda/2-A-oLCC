class Reserva:
    __numero = int
    __nombre = str
    __numCabana = int
    __fecha = str
    __cantHuespedes = int
    __cantDias = int
    __sena = float

    def __init__(self, numero, nombre, numcabana, fecha, canthuespedes, cantdias, sena):
        self.__numero = int(numero)
        self.__nombre = nombre
        self.__numCabana = int(numcabana)
        self.__fecha = fecha
        self.__cantHuespedes = int(canthuespedes)
        self.__cantDias = int(cantdias)
        self.__sena = float(sena)

    def getnumeroreserva(self):
        return self.__numero

    def getnombre(self):
        return self.__nombre

    def getnumcabana(self):
        return self.__numCabana

    def getfecha(self):
        return self.__fecha

    def getcanthuespedes(self):
        return self.__cantHuespedes

    def getcantdias(self):
        return self.__cantDias

    def getsena(self):
        return self.__sena
