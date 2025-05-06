class Nacimiento:
    __dni: int
    __tipo: str
    __fecha: str
    __hora: str
    __peso: float
    __altura: float
    def __init__(self, dni, tipo, fecha, hora, peso, altura):
        self.__dni = dni
        self.__tipo = tipo
        self.__fecha = fecha
        self.__hora = hora
        self.__peso = peso
        self.__altura = altura
    def ObtenerDni(self):
        return self.__dni
    def ObtenerTipo(self):
        return self.__tipo
    def ObtenerPeso(self):
        return self.__peso
    def ObtenerAltura(self):
        return self.__altura
    def ObtenerFecha(self):
        return self.__fecha
    def __eq__(self, otro):
        band = False
        if (self.__dni == otro.__dni)and(self.__fecha == otro.__fecha):
            band = True
        return band