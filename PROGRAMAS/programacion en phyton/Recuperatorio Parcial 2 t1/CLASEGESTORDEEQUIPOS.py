from CLASEEQUIPOS import Equipos
from CLASEHERRAMIENTASELECTRICAS import HerramientasElectricas
from CLASEMAQUINARIAPESADA import MaquinariaPesada
from CLASENODO import Nodo
import csv

class GestoreDeEquipos:
    __comienzo : Nodo
    __actual : Nodo
    __indice : int
    __tope : int
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def __iter__(self):
        self.__indice = 0
        self.__actual = self.__comienzo
        return self
    def __next__(self):
        if self.__actual == None:
            raise StopIteration
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    def __getTope(self):
        return self.__tope  
    
    def agregarEquipo(self, equipo):
        nodo = Nodo(equipo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo =  nodo
        self.__actual = nodo
        self.__tope += 1

    def cargarEquipos(self):
        archivo = open("equipos.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if (fila[0] == "M"):
                Nequipo = MaquinariaPesada(fila[1], fila[2], int(fila[3]), fila[4], fila[5], float(fila[6]), float(fila[7]), int(fila[8]), fila[9], float(fila[10]))
                self.agregarEquipo(Nequipo)
            elif (fila[0] == "E"):
                Nequipo = HerramientasElectricas(fila[1], fila[2], int(fila[3]), fila[4], fila[5], fila[6], float(fila[7]), int(fila[8]), fila[9])
                self.agregarEquipo(Nequipo)
        archivo.close

    def mostrarTipoPlan(self, pos):
        aux = self.__comienzo
        self.__actual = 0
        while self.__actual < pos and aux is not None:
            aux = aux.getSiguiente()
            self.__actual+=1
        if aux is not None:
            if isinstance(aux.getDato(), MaquinariaPesada):
                print(f"El equipo almacenado en la posición: {pos} es del tipo: Maquinaria Pesada")
            elif isinstance(aux.getDato(), HerramientasElectricas):
                print(f"El equipo almacenado en la posición: {pos} es del tipo: Herramientas Electricas")
        else:
            raise IndexError("Índice fuera de rango")
    
    def contarHerramientasElectricas(self, ano):
        aux = self.__comienzo
        c = 0
        while aux is not None:
            if isinstance(aux.getDato(), HerramientasElectricas):
                if aux.getDato().getAnoFab() == ano:
                    c += 1
            aux = aux.getSiguiente()
        print(f"Existen {c} equipos con un año de fabricación de {ano}")

    def contarEquiposConCapacidadCarga(self, capacidad):
        aux = self.__comienzo
        c = 0
        while aux is not None:
            if isinstance(aux.getDato(), MaquinariaPesada):
                if aux.getDato().getCapCarga() <= capacidad:
                    c += 1
            aux = aux.getSiguiente()
        print(f"Existen {c} equipos con una capacidad de carga menor o igual a {capacidad} toneladas")

    def mostrarEquipos(self):
        aux = self.__comienzo
        while aux is not None:
            if aux.getDato().getTipoCombustible() != "N/A" and aux.getDato().getCapCarga() != "N/A":
                print(f"Marca: {aux.getDato().getMarca()} Modelo: {aux.getDato().getModelo()} Año de fabricación: {aux.getDato().getAnoFab()} Tipo de combustible: {aux.getDato().getTipoCombustible()} Potencia: {aux.getDato().getPotencia()} Capacidad de carga: {aux.getDato().getCapCarga()} Tarifa de alquiler: {aux.getDato().calcularAlquiler()}")
            elif aux.getDato().getTipoCombustible() != "N/A" and aux.getDato().getCapCarga() == "N/A":
                print(f"Marca: {aux.getDato().getMarca()} Modelo: {aux.getDato().getModelo()} Año de fabricación: {aux.getDato().getAnoFab()} Tipo de combustible: {aux.getDato().getTipoCombustible()} Potencia: {aux.getDato().getPotencia()} Tarifa de alquiler: {aux.getDato().calcularAlquiler()}")
            elif aux.getDato().getTipoCombustible() == "N/A" and aux.getDato().getCapCarga() != "N/A":
                print(f"Marca: {aux.getDato().getMarca()} Modelo: {aux.getDato().getModelo()} Año de fabricación: {aux.getDato().getAnoFab()} Potencia: {aux.getDato().getPotencia()} Capacidad de carga: {aux.getDato().getCapCarga()} Tarifa de alquiler: {aux.getDato().calcularAlquiler()}")
            else:
                print(f"Marca: {aux.getDato().getMarca()} Modelo: {aux.getDato().getModelo()} Año de fabricación: {aux.getDato().getAnoFab()} Potencia: {aux.getDato().getPotencia()} Tarifa de alquiler: {aux.getDato().calcularAlquiler()}")
            aux = aux.getSiguiente()