from CLASEVEHICULOS import vehiculo
class autobus(vehiculo):
    __tipo : str
    __turno : str
    def __init__(self, marca, modelo, anoFab, capacidad, numPlazas, distancia, tarifa,  tipo, turno):
        super().__init__(marca, modelo, anoFab, capacidad, numPlazas, distancia, tarifa)
        self.__tipo = tipo
        self.__turno = turno
    def CalcularTarifa(self):
        if(self.__tipo == "turismo")and(self.__turno == "noche"):
            return (self.getTarifaBase()*1.2)
        else:
            return (float(self.getTarifaBase())*1.05)