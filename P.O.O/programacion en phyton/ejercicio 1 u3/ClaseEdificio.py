from ClaseDepartamento import Departamento
class Edificio:
    __id : int
    __nombre : str
    __direc : str
    __empresa : str
    __cpisos : int
    __cdeptos : int
    __departamentos : list

    def __init__(self, id, nombre, direc, empresa, cpisos, cdeptos):
        self.__id = id
        self.__nombre = nombre
        self.__direc = direc
        self.__empresa = empresa
        self.__cpisos = cpisos
        self.__cdeptos = cdeptos
        self.__departamentos = []

    def obtenerId(self):
        return self.__id
    
    def obtenerNombre(self):
        return self.__nombre
    
    def agregarDepto(self, depto):
        d = Departamento(depto.obtenerId(), depto.obtenerNyA(), depto.obtenerNumPiso(), depto.obtenerNumDepto(), depto.obtenerChab(), depto.obtenerCbanos(), depto.obtenerSup())
        self.__departamentos.append(d)

    def nombresPropietarios(self):
        for departamento in self.__departamentos:
            print(f"Propietario: {departamento.obtenerNyA()}\n")

    def calcularSuperficie(self):
        superficie = 0
        for departamento in self.__departamentos:
            superficie += departamento.obtenerSup()
        return superficie
    
    def supPropietario(self, nomPropietario):
        supEdificio = self.calcularSuperficie()
        for departamento in self.__departamentos:
            if departamento.obtenerNyA() == nomPropietario:
                print(f"Superficie del departamento id {departamento.obtenerNumDepto()}: {departamento.obtenerSup()}\n Representa el {round(((departamento.obtenerSup()*100)/supEdificio), 2)}% del total de la superficie del edificio")

    def contarDepartamentos(self, numPiso):
        cont = 0
        for departamento in self.__departamentos:
            if departamento.obtenerNumPiso() == numPiso and departamento.obtenerCbanos() > 1:
                cont += 1
        return cont
