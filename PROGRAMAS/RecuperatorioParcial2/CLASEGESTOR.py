import csv
from CLASENODO import Nodo
from CLASEPLANTELEFONIA import ptelefonia
from CLASEPLANTELEVISION import ptelevision

class gestor:
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
    def AgregarPlan(self, plan):
        nodo= Nodo(plan)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def CargarPlanes(self):
        archivo=open("planes.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if (fila[0] == "M"):
                Nptelefonia = ptelefonia(fila[1], int(fila[2]), fila[3], float(fila[4]), fila[5], int(fila[6]))
                self.AgregarPlan(Nptelefonia)
            elif (fila[0] == "T"):
                Nptelevision = ptelevision(fila[1], int(fila[2]), fila[3], float(fila[4]), int(fila[5]), int(fila[6]))
                self.AgregarPlan(Nptelevision)
        archivo.close
    def MostrarTipoPlan(self, pos):
        if pos < self.__getTope():
            aux = self.__comienzo
            for i in range(pos):
                aux = aux.getSiguiente()
            if isinstance(aux.getDato(), ptelefonia):
                print(f"El tipo de plan de la posicion ingresada es -Telefónico-")
            if isinstance(aux.getDato(), ptelevision):
                print(f"El tipo de plan de la posicion ingresada es -Televisión-")
        else:
            raise IndexError
            
    def ContarPlanes(self, zona):
        c = 0
        aux = self.__comienzo
        while aux is not None:
            if aux.getDato().ObtenerCobertura() == zona:
                c += 1
                print(f"El plan de la compañia{aux.getDato().ObtenerNombre()} tiene cobertura en {zona}")
            aux=aux.getSiguiente()
        print(f"Existen {c} planes con cobertura: {zona}")
    
    def BuscarPlanesInternacionales(self, cant):
        aux = self.__comienzo
        band = False
        while aux is not None:
            if isinstance(aux.getDato(),ptelevision):
                nuevaCant = int(aux.getDato().ObtenerCantInter())
                if nuevaCant >= cant:
                    if band == False:
                        band = True
                        print("Las compañias con un numero de canales internacionales mayor o igual al ingresado son:")
                    print(f"Compañía: {aux.getDato().ObtenerNombre()}")
            aux = aux.getSiguiente()
                
    def MostrarPlanes(self):
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), ptelefonia):
                print(f"Tipo de plan: Telefonía          Compañía: {aux.getDato().ObtenerNombre()}          Duración: {aux.getDato().ObtenerDuracion()}          Cobertura: {aux.getDato().ObtenerCobertura()}          Importe: {aux.getDato().CalcularImporte()}")
            elif isinstance(aux.getDato(), ptelevision):
                print(f"Tipo de plan: Televisión          Compañía: {aux.getDato().ObtenerNombre()}          Duración: {aux.getDato().ObtenerDuracion()}          Cobertura: {aux.getDato().ObtenerCobertura()}          Importe: {aux.getDato().CalcularImporte()}")
            aux = aux.getSiguiente()
