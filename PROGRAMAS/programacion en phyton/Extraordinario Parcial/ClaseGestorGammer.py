from ClaseNodo import Nodo
from ClaseGammer import Gammer
import csv
class GestorGammer:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def __getTope(self):
        return self.__tope
    def AgregarGammer(self, gammer):
        nodo= Nodo(gammer)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def CargarGammers(self):
        archivo=open("gammers.csv")
        reader=csv.reader(archivo, delimiter=";")
        for fila in reader:
                Ngammer = Gammer(int(fila[0]), int(fila[1]), fila[2], fila[3], fila[4], fila[5], float(fila[6]), int(fila[7]))
                self.AgregarGammer(Ngammer)
        archivo.close
    def BuscarGammer(self, dni, ContenedorConexiones):
        c = 0
        band = False
        aux = self.__comienzo
        while aux is not None and band == False:
            print ("DNI---->",aux.getDato().getDni())
            if dni == aux.getDato().getDni():
                print(f"DNI: {dni}         Nombre y Apellido: {aux.getDato().getNombre()} {aux.getDato().getApellido()}")
                print(f"Alias: {aux.getDato().getAlias()}       Plan: {aux.getDato().getPlan()}       Importe base: {aux.getDato().getImporteBase()}")
                ContenedorConexiones.MostrarConexiones(aux.getDato().getId())
                band = True
        if band == False:
            print("El DNI ingresado no corresponde a un gammer")
