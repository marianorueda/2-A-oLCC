from ClaseClienteLocal import ClienteLocal
from ClaseClienteNacional import ClienteNacional
from ClaseNodo import Nodo

class Coleccion():
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
        self.__indice = 0
        self.__actual = self.__comienzo
        return self
    def __next__(self):
        if self.__actual == None:
            raise StopIteration
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def __getTope(self):
        return self.__tope
    
    def insertarAlFinal(self,clienteLocal):
        nuevoNodo = Nodo(clienteLocal)
        if self.__comienzo == None:
            self.__comienzo = nuevoNodo
        else:
            actual = self.__comienzo
            while actual.getSiguiente() != None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nuevoNodo)
        self.__tope+=1

    def mostrarClientesNacionales(self):
        i=0
        for i in self:
            if isinstance(i, ClienteNacional):
                print(f"Nombre: {i.getNombre()} Provincia: {i.getProvincia()}")

    def buscarPosicion(self, pos):
        aux = self.__comienzo
        self.__actual = 0
        while self.__actual < pos and aux is not None:
            aux = aux.getSiguiente()
            self.__actual+=1
        if aux is not None:
            print(f"La posicion {pos} esta ocupada por el cliente {aux.getDato().getNombre()}")
        else:
            print(f"La posicion {pos} no corresponde a ningun cliente")

    def mostrar(self):
        aux = self.__comienzo
        while aux is not None:
            print(f"Nombre: {aux.getDato().getNombre()} Apellido: {aux.getDato().getApellido()}")
            aux = aux.getSiguiente()