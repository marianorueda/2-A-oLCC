from ClaseClienteLocal import ClienteLocal

class ClienteNacional(ClienteLocal):
    __provincia : str
    __localidad : str 
    __codigoPostal : int
    def __init__(self, nombre, apellido, email, contrasena, direccion, telefono, provincia, localidad, codigoPostal):
        super().__init__(nombre, apellido, email, contrasena, direccion, telefono)
        self.__provincia = provincia
        self.__localidad = localidad
        self.__codigoPostal = codigoPostal
        
    def getProvincia(self):
        return self.__provincia

    def getLocalidad(self):
        return self.__localidad

    def getCodigoPostal(self):
        return self.__codigoPostal