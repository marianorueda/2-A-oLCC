from CLASEPACIENTE import Paciente

class PacienteHospitalizado(Paciente):
    __numHab : int
    __fechaIngreso : str
    __diagnostico : str
    __cDias : int
    __importeDescartables : float
    def __init__(self, nombre, apellido, email, telefono, numHab, fechaIngreso, diagnostico, cDias, importeDescartables):
        super().__init__(nombre, apellido, email, telefono)
        self.__numHab = numHab
        self.__fechaIngreso = fechaIngreso
        self.__diagnostico = diagnostico
        self.__cDias = cDias
        self.__importeDescartables = importeDescartables

    def getNumHab(self):
        return self.__numHab
    
    def getFechaIngreso(self):
        return self.__fechaIngreso
    
    def getDiagnostico(self):
        return self.__diagnostico
    
    def getCDias(self):
        return self.__cDias
    
    def getImporteDescartables(self):
        return self.__importeDescartables
    
    def calcularImporte(self):
        return self.__cDias * 150000 + self.__importeDescartables