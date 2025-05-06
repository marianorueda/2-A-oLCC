import csv
from ModuloreservaJOSE import Reserva


class gestorreserva:
    __gestorReserva = list

    def __init__(self):
        self.__gestorReserva = []
        archivo = open("Reservas[1]JOSE.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True
            else:
                numero = int(fila[0])
                nombre = fila[1]
                numeroc = int(fila[2])
                fecha = fila[3]
                canth = int(fila[4])
                cantd = int(fila[5])
                sena = float(fila[6])
                nuevoreserva = Reserva(
                    numero, nombre, numeroc, fecha, canth, cantd, sena)
                self.__gestorReserva.append(nuevoreserva)
        archivo.close()
    def BuscarNumCabana(self, NumCabana):
        i=0
        while (i<len(self.__gestorReserva)):
            if NumCabana==self.__gestorReserva[i].getnumcabana():
                return False
            i+=1
        return True