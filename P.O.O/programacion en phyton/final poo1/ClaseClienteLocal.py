class ClienteLocal:
    __nombre : str
    __apellido : str
    __direccion : str
    __telefono : str
    __email : str
    __contrasena : str

    def __init__(self, nombre, apellido, email, contrasena, direccion, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__contrasena = contrasena
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono
    
    def getEmail(self):
        return self.__email
    
    def getContrasena(self):
        return self.__contrasena