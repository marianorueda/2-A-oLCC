class Mama:
    __dni: int
    __edad: int
    __AyN: str
    def __init__(self, dni, edad, Ayn):
        self.__dni = dni
        self.__edad = edad
        self.__AyN = Ayn
    def ObtenerDni(self):
        return self.__dni
    def ObtenerNom(self):
        return self.__AyN
    def ObtenerEdad(self):
        return self.__edad
    