class Cabana:
    __numero = int
    __cantHab = int
    __cantCamG = int
    __cantCamC = int
    __importe = float

    def __init__(self, numero, cantHab, cantCamG, cantCamC, importe):
        self.__numero = int(numero)
        self.__cantHab = int(cantHab)
        self.__cantCamG = int(cantCamG)
        self.__cantCamC = int(cantCamC)
        self.__importe = float(importe)

    def getnumero(self):
        return self.__numero

    def getcanthab(self):
        return self.__cantHab

    def getcantcamg(self):
        return self.__cantCamG

    def getcantcamc(self):
        return self.__cantCamC

    def getimporte(self):
        return self.__importe

    def __ge__(self, num):
        return (self.__cantCamG * 2 + self.__cantCamC) >= num
