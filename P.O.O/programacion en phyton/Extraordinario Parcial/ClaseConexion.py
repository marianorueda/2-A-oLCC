class Conexion:
    __id : int
    __direccionIp : str
    __nombreJuego : str
    __fecha : str
    __horaIni : int
    __horaFin : int
    def __init__(self, id, direccionIp, nombreJuego, fecha, horaIni, horaFin):
        self.__id = id
        self.__direccionIp = direccionIp
        self.__nombreJuego = nombreJuego
        self.__fecha = fecha
        self.__horaIni = horaIni
        self.__horaFin = horaFin

    def getId(self):
        return self.__id

    def getDireccionIp(self):
        return self.__direccionIp

    def getNombreJuego(self):
        return self.__nombreJuego

    def getFecha(self):
        return self.__fecha

    def getHoraIni(self):
        return self.__horaIni

    def getHoraFin(self):
        return self.__horaFin