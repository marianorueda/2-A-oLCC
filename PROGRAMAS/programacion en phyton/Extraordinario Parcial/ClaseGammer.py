class Gammer:
    __id : int
    __dni : int
    __nombre : str
    __apellido : str
    __alias : str
    __plan : str
    __importeBase : float
    __tiempoLimite : int

    def __init__(self, id, dni, nombre, apellido, alias, plan, importeBase, tiempoLimite):
        self.__id = id
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__alias = alias
        self.__plan = plan
        self.__importeBase = importeBase
        self.__tiempoLimite = tiempoLimite

    def getId(self):
        return self.__id

    def getDni(self):
        return self.__dni

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getAlias(self):
        return self.__alias

    def getPlan(self):
        return self.__plan

    def getImporteBase(self):
        return self.__importeBase

    def getTiempoLimite(self):
        return self.__tiempoLimite