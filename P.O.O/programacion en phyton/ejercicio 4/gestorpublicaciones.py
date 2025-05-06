from libros import libro
from cds import cd
import csv
class gestor:
    __lista : list
    def __init__(self):
        self.__lista = []
    def agregarCds(self):
        archivo = open("CDs.csv", "r")
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            ncd=cd(fila[0], fila[1], float(fila[2]), int(fila[3]), fila[4])
            self.__lista.append(ncd)
        archivo.close()
    def agregarLibros(self):
        archivo = open("Libros.csv", "r")
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            nlibro=libro(fila[0], fila[1], float(fila[2]), fila[3], int(fila[4]), int(fila[5]))
            self.__lista.append(nlibro)
        archivo.close()
    def buscarTipo(self, pos):
        long = len(self.__lista)
        while pos<-1 or pos>=long:
            pos = int(input("Posicion erronea, Ingrese una nueva posicion de la publicacion en la lista (Si quiere regresar al menu ingrese [-1])"))
        if pos>=0:
            publi = self.__lista[pos]
            if isinstance(publi, libro):
                print("La publicacion de la posicion ingresada es un Libro")
            if isinstance(publi, cd):
                print("La publicacion de la posicion ingresada es un CD")
    def contarPublicaciones(self):
        cl = 0
        cc = 0
        i = 0
        long = len(self.__lista)
        for i in range (long):
            if isinstance(self.__lista[i], libro):
                cl += 1
            elif isinstance(self.__lista[i], cd):
                cc += 1
        print(f"Hay {cl} libros y {cc} CDs")
    def mostrar(self):
        i = 0
        long = len(self.__lista)
        for i in range (long):
            print(f"Título: {self.__lista[i].getTitulo()}, Categoria: {self.__lista[i].getCategoria()}, Importe de venta: {self.__lista[i].calcularImporte()}")

    