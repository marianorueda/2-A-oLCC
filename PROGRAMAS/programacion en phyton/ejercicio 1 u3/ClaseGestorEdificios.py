from ClaseEdificio import Edificio, Departamento
import csv

class GestorEdificios:
    __lista : list
    def __init__(self):
        self.__lista = []
        archivo = open("EdificioNorte.csv")
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            if len(fila) == 6:
                id = int(fila[0])
                nombre = fila[1]
                direc = fila[2]
                empresa = fila[3]
                cpisos = int(fila[4])
                cdeptos = int(fila[5])
                edificio = Edificio(id, nombre, direc, empresa, cpisos, cdeptos)
                self.__lista.append(edificio)
            else:
                id = int(fila[1])
                NyA = fila[2]
                numPiso = int(fila[3])
                numDepto = int(fila[4])
                chab = int(fila[5])
                cbanos = int(fila[6])
                sup = float(fila[7])
                departamento = Departamento(id, NyA, numPiso, numDepto, chab, cbanos, sup)
                edificio.agregarDepto(departamento)
        archivo.close()
    def mostrarPropietarios(self, idEdificio):
        i = 0
        while i < len(self.__lista) and idEdificio != self.__lista[i].obtenerId():
            i += 1
        if i < len(self.__lista):
            self.__lista[i].nombresPropietarios()
        else:
            print("El id ingresado no corresponde a un edificio")
    def buscarSuperficie(self, nomEdificio):
        i = 0
        while i < len(self.__lista) and nomEdificio != self.__lista[i].obtenerNombre():
            i += 1
        if i < len(self.__lista):
            print(f"Superficie: {self.__lista[i].calcularSuperficie()}")
        else:
            print("El nombre ingresado no corresponde a un edificio")
    def deptosSuperficie(self, nomPropietario):
        for edificio in self.__lista:
            edificio.supPropietario(nomPropietario)
    def buscarDepartamentos(self, numPiso):
        for edificio in self.__lista:
            cont = edificio.contarDepartamentos(numPiso)
        print(f"Existen {cont} departamentos con 3 dormitorios y mas de un baño en el piso {numPiso}")



