import csv
from ModuloNacimientos import Nacimiento

class gestorNacimientos:
    __lista: list
    def __init__(self):
        self.__lista = []
        archivo = open("Nacimientos.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            dni = int(fila[0])
            tipo = fila[1]
            fecha = fila[2]
            hora = fila[3]
            peso = fila[4]
            altura = float(fila[5])
            nacimiento = Nacimiento(dni, tipo, fecha, hora, peso, altura)
            self.__lista.append(nacimiento)
        archivo.close()
    def MostrarNacimientos(self, dni):
        i=0
        band=0
        for i in range (len(self.__lista)):
            if dni == self.__lista[i].ObtenerDni():
                if(band==0):
                    print(f"Tipo de Parto: {self.__lista[i].ObtenerTipo()}")
                    print("Bebé/s: \n  Peso:          Altura:")
                print(f"  {self.__lista[i].ObtenerPeso()}          {self.__lista[i].ObtenerAltura()}")
                band=1
    def ObtenerLista(self):
        return self.__lista
    def PartosMultiples(self, dni):
        i = 0
        c = 0
        while (i < len(self.__lista))and(c == 0):
            if dni == (self.__lista[i].ObtenerDni()):
                c = 1
            else: 
                i += 1
        if c == 1:
            j = i + 1
            while j < len(self.__lista):
                if self.__lista[i] == self.__lista[j]:
                    c += 1
                j += 1
        return c