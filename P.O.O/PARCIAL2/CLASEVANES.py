from CLASEVEHICULOS import vehiculo
class van(vehiculo):
    __tipo : str
    def __init__(self, marca, modelo, anoFab, capacidad, numPlazas, distancia, tarifa, tipo):
        super().__init__(marca, modelo, anoFab, capacidad, numPlazas, distancia, tarifa)
        self.__tipo = tipo
    def CalcularTarifa(self):
        if(self.__tipo == "minivan"):
            return (self.getTarifaBase()*0.9)
        else:
            return (float(self.getTarifaBase()*1.025))