import numpy as np
class gestor:
    def __init__(self):
        self.__matriz = np.zeros((5,7))
    def CargarDatos(self):
        sucursal = int(input("Ingrese numero de sucursal: \n"))
        dia = int(input("Ingrese dia de la semana: \n"))
        self.__matriz[sucursal - 1][dia -1] += float(input("Ingrese importe de la factura: \n"))
    def CalcularFacturacion(self):
        sucursal = int(input("Ingrese numero de sucursal: \n"))
        total = 0
        for i in range (6):
            total += self.__matriz[sucursal - 1]
        print(f"Total facturado para la sucursal {sucursal}, es: {total}")
    def MayoresVentas(self):
        dia = ("Ingrese dia de la semana")
        if(dia == "lunes"):
            imax = np.argmax(self.__matriz[:,0], axis = 0)
        elif(dia == "martes"):
            imax = np.argmax(self.__matriz[:,1], axis = 0)   
        elif(dia == "miercoles"):
            imax = np.argmax(self.__matriz[:,2], axis = 0)
        elif(dia == "jueves"):
            imax = np.argmax(self.__matriz[:,3], axis = 0)
        elif(dia == "viernes"):
            imax = np.argmax(self.__matriz[:,4], axis = 0)
        elif(dia == "sabado"):
            imax = np.argmax(self.__matriz[:,5], axis = 0)
        elif(dia == "domingo"):
            imax = np.argmax(self.__matriz[:,6], axis = 0)
        #print(f"El dia {dia}, la sucursal que mas facuro fue la n°:", imax)
    def MenoresVentas(self):
        sum=0
        min = 99999999999999999
        for i in range(5):
            for j in range(7):
                sum += self.__matriz[i][j]
            if sum<min:
                min = sum
                pos_min_i = i
            sum = 0
        print(f"La sucursal que menos vendio en la semana fue la n°: {pos_min_i} \n")
    def TotalSemanal(self):
        sum=0
        for i in range(5):
            for j in range(7):
                sum += self.__matriz[i][j]
        print(f"El total vendido en la semana fue de: {sum} \n")
    

    