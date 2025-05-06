from CLASEPACIENTE import Paciente

class PacienteAmbulatorio(Paciente):
    __historialMed : str
    __alergias : str
    __obraSocial : str
    def __init__(self, nombre, apellido, email, telefono, historialMed, alergias, obraSocial):
        super().__init__(nombre, apellido, email, telefono)
        self.__historialMed = historialMed
        self.__alergias = alergias
        self.__obraSocial = obraSocial

    def getHistorialMed(self):
        return self.__historialMed
    
    def getAlergias(self):
        return self.__alergias
    
    def getObraSocial(self):
        return self.__obraSocial
    
    def calcularImporte(self):
        if self.getObraSocial() == "Obra Social Provincia":
            return self.getValorConsulta() - 15000 + 5000
        elif self.getObraSocial() == "OSDE":
            return self.getValorConsulta() - 15000 + 2000
        else: 
            return self.getValorConsulta() - 15000 + 10000