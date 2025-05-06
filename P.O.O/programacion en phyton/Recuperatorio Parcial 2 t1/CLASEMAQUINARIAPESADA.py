from CLASEEQUIPOS import Equipos

class MaquinariaPesada(Equipos):
    __tipo : str
    __peso : float
    def __init__(self, marca, modelo, anoFab, tipoCombustible, potencia, capCarga, tarifa, cDias, tipo, peso):
        super().__init__(marca, modelo, anoFab, tipoCombustible, potencia, capCarga, tarifa, cDias)
        self.__tipo = tipo
        self.__peso = peso

    def getTipo(self):
        return self.__tipo
    
    def calcularAlquiler(self):
        if self.__peso <= 10:
            return self.getTarifa() * self.getCDias()
        else:
            return self.getTarifa() * self.getCDias() * 1.2