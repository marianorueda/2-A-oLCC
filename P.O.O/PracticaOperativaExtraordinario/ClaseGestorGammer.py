import csv
from ClaseGamer import Gammer

class GestorDeGammer:
    __lista: list
    def __init__(self):
        self.__lista = []
        archivo = open("gammers.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if fila[0] != "idjugador":
                id = int(fila[0])
                dni = int(fila[1])
                nombre = fila[2]
                apellido = fila[3]
                alias = fila[4]
                plan = fila[5]
                importeBase = float(fila[6])
                tiempoLimite = int(fila[7])
                gammer = Gammer(id, dni, nombre, apellido, alias, plan, importeBase, tiempoLimite)
                self.__lista.append(gammer)
        archivo.close()