from CLASEEQUIPOS import Equipos

class HerramientasElectricas(Equipos):
    __tipo : str
    def __init__(self, marca, modelo, anoFab, tipoCombustible, potencia, capCarga, tarifa, cDias, tipo):
        super().__init__(marca, modelo, anoFab, tipoCombustible, potencia, capCarga, tarifa, cDias)
        self.__tipo = tipo

    def getTipo(self):
        return self.__tipo

    def calcularAlquiler(self):
        if self.__tipo == "bateria":
            return self.getTarifa() * self.getCDias() * 1.1
        else:
            return self.getTarifa() * self.getCDias()