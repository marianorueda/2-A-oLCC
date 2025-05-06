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
    def MostrarPartosMultiples(self, gestorMamas):
        multiples = []
        i = 0
        while i < len(self.__lista):
            nacimiento = self.__lista[i]
            j = 0
            while j < len(multiples):
                if multiples[j][0] == nacimiento:  
                    multiples[j].append(nacimiento)
                    break
                j += 1
            else:
                multiples.append([nacimiento])
            i += 1
        i = 0
        while i < len(multiples):
            partoMultiple = multiples[i]
            if len(partoMultiple) > 1:
                j = 0
                while j < len(gestorMamas.ObtenerArreglo()):
                    mama = gestorMamas.ObtenerArreglo()[j]
                    if mama.ObtenerNom() == partoMultiple[0].ObtenerDni():
                        print(f"Mamá: {mama.ObtenerNom()}, DNI: {mama.ObtenerDni()}, Edad: {mama.ObtenerEdad()}")
                        print(f"Fecha de parto múltiple: {partoMultiple[0].ObtenerFecha()}")
                        k = 0
                        while k < len(partoMultiple):
                            nacimiento = partoMultiple[k]
                            print(f"  Tipo de parto: {nacimiento.ObtenerTipo()}, Peso: {nacimiento.ObtenerPeso()}, Altura: {nacimiento.ObtenerAltura()}")
                            k += 1
                        break
                    j += 1
            i+=1