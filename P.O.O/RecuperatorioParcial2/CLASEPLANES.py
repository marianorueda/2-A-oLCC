import abc
class plan:
    __nombre : str
    __duracion : str
    __cobertura : str
    __precio : float
    def __init__(self, nombre, duracion, cobertura, precio):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__cobertura = cobertura
        self.__precio = precio
    def ObtenerPrecio(self):
        return self.__precio
    def ObtenerNombre(self):
        return self.__nombre
    def ObtenerCobertura(self):
        return self.__cobertura
    def ObtenerDuracion(self):
        return self.__duracion
    @abc.abstractmethod
    def CalcularImporte(self):
        pass