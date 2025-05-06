class Conexion:
    __id : int
    __direccionIP: str
    __nombreJuego: str
    __fecha: str
    __horaInicio: int
    __horaFin: int
    def __init__(self, id, direccionIP, nombreJuego, fecha, horaInicio, horaFin):
        __id = id
        __direccionIP = direccionIP
        __nombreJuego = nombreJuego
        __fecha = fecha
        __horaInicio = horaInicio
        __horaFin = horaFin
    def __eq__(self, otro):
        band = False
        if (self.__id == otro.__id)and(self.__fecha == otro.__fecha)and(self.__horaInicio == otro.__horaInicio)and(self.__direccionIP != otro.__direccionIP):
            band = True
        return band
    def __lt__(self, otro):
        if self.__id != otro.__id:
            return self.__id < otro.__id
        elif self.__fecha != otro.__fecha:
            return self.__fecha < otro.__fecha
        elif self.__horaInicio != otro.__horaInicio:
            return self.__horaInicio < otro.__horaInicio
        elif self.__direccionIP != otro.__direccionIP:
            return self.__direccionIP < otro.__direccionIP
