from CLASEPACIENTE import Paciente
from CLASEPACIENTEAMBULATORIO import PacienteAmbulatorio
from CLASEPACIENTEHOSPITALIZADO import PacienteHospitalizado
from CLASENODO import Nodo
import csv

class Coleccion():
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int
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
    
    def agregarPaciente(self, paciente):
        nodo = Nodo(paciente)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo =  nodo
        self.__actual = nodo
        self.__tope += 1

    def cargarPacientes(self):
        archivo = open("pacientes.csv")
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if (fila[0] == "P"):
                Npaciente = Paciente(fila[1], fila[2], fila[3], int(fila[4]))
                self.agregarPaciente(Npaciente)
            elif (fila[0] == "O"):
                Npaciente = PacienteAmbulatorio(fila[1], fila[2], fila[3], int(fila[4]), fila[5], fila[6], fila[7])
                self.agregarPaciente(Npaciente)
            elif (fila[0] == "H"):
                Npaciente = PacienteHospitalizado(fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]), fila[6], fila[7], int(fila[8]), float(fila[9]))
                self.agregarPaciente(Npaciente)
        archivo.close

    def insertarAlFinal(self, paciente):
        nuevoNodo = Nodo(paciente)
        if self.__comienzo == None:
            self.__comienzo = nuevoNodo
        else:
            actual = self.__comienzo
            while actual.getSiguiente() != None:
                actual = actual.getSiguiente()
            actual.setSiguiente(nuevoNodo)
        self.__tope+=1
    
    def contarPacientesNeumonia(self):
        i = 0
        c = 0
        for i in self:
            if isinstance(i, PacienteHospitalizado):
                if i.getDiagnostico() == "Neumonia":
                    c += 1
        print(f"Hay {c} pacientes hospitalizados con diagnostico de neumonia")

    def contarPacientesAmbulatorios(self):
        i = 0
        c = 0
        for i in self:
            if isinstance(i, PacienteAmbulatorio):
                c += 1
        print(f"Hay {c} pacientes ambulatorios en la clínica")
    
    def mostrarImportes(self):
        i = 0
        for i in self:
            print(f"Paciente: {i.getNombre()} {i.getApellido()} Importe: {i.importeTotal()}")
            
    def determinarTipoPaciente(self, pos):
        aux = self.__comienzo
        self.__actual = 0
        while self.__actual < pos and aux is not None:
            aux = aux.getSiguiente()
            self.__actual += 1
        if aux is not None:
            if isinstance(aux.getDato(), PacienteAmbulatorio):
                print(f"La posicion {pos} esta ocupada por un Paciente Ambulatorio con Obra Social")
            elif isinstance(aux.getDato(), PacienteHospitalizado):
                print(f"La posicion {pos} esta ocupada por un Paciente Hospitalizado")
            elif isinstance(aux.getDato(), Paciente):
                print(f"La posicion {pos} esta ocupada por un Paciente normal")
        else:
            raise IndexError("Indice fuera de rango")
    
    def modificarValorConsulta(self, valor):
        for i in self:
            pepe = Paciente()
            pepe = Paciente(i.getNombre(), i.getApellido(), i.getEmail(), i.getTelefono())
            pepe.cambiarValorConsulta(valor)
    


























