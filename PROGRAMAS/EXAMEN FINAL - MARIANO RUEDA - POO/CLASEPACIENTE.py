import abc

class Paciente():
    __nombre : str
    __apellido : str
    __email : str
    __telefono : int
    __valorConsulta = staticmethod = 15000
    def __init__(self, nombre = "", apellido = "", email = "", telefono = 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__telefono = telefono


    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getTelefono(self):
        return self.__telefono
    
    def getValorConsulta(self):
        return self.__valorConsulta
    
    @abc.abstractmethod
    def calcularImporte(self):
        pass

    @classmethod
    def cambiarValorConsulta(cls, valor):
        cls.__valorConsulta = valor

    def importeTotal(self):
        imp = 0
        if self.calcularImporte() != None:
            imp = self.calcularImporte()
        return self.__valorConsulta + float(imp)