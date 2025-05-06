import csv
from Movimientos import GestorMovimientos

class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numCuenta: int
    __saldoAnt: float
    def __init__(self, nombre, apellido, dni, numCuenta, saldoAnt):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__numCuenta=numCuenta
        self.__saldoAnt=saldoAnt
    def ObtenerDni(self):
        return self.__dni
    def ObtenerNombre(self):
        return self.__nombre
    def ObtenerApellido(self):
        return self.__apellido
    def ObtenerSaldoAnt(self):
        return self.__saldoAnt
    def ObtenerNumCuenta(self):
        return self.__numCuenta
    def ActualizarSaldo(self, diferencia):
        self.__saldoAnt+=diferencia

class GestorClientes:
    __lista: list

    def __init__(self):
        self.__lista = []
        archivo = open("ClientesFarmaCiudad.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            nombre = fila[0]
            apellido = fila[1]
            dni = int(fila[2])
            numCuenta = int(fila[3])
            saldoAnt = float(fila[4])
            cliente = Cliente(nombre, apellido, dni, numCuenta, saldoAnt)
            self.__lista.append(cliente)
        archivo.close()

    def BuscarCliente(self, dni):
        i=0
        while (dni != self.__lista[i].ObtenerDni()) and (i<len(self.__lista)):
            i+=1
        if (dni == self.__lista[i].ObtenerDni()):
            return i
        else:
            return -1
        
    def ActualizarCliente(self, i, GestorMovimientos):
        print(f"Cliente: {self.__lista[i].ObtenerNombre()} {self.__lista[i].ObtenerApellido()}        Numero de Cuenta: {self.__lista[i].ObtenerNumCuenta()}")
        print(f"Saldo Anterior: {self.__lista[i].ObtenerSaldoAnt()}")
        print("Movimientos:")
        print("Fecha          Descripción          Importe          Tipo de Movimiento")
        diferencia = GestorMovimientos.CalcularMovimientos(self.__lista[i].ObtenerNumCuenta())
        self.__lista[i].ActualizarSaldo(diferencia)
        print(f"Saldo Actualizado: {self.__lista[i].ObtenerSaldoAnt()}")

    def InformeCliente(self, i, GestorMovimientos):
        if GestorMovimientos.ConsultarMovimientos(self.__lista[i].ObtenerNumCuenta()) == 1:
            print(f"El Cliente {self.__lista[i].ObtenerNombre()} {self.__lista[i].ObtenerApellido()} si tuvo movimientos")
        else:
            print(f"El Cliente {self.__lista[i].ObtenerNombre()} {self.__lista[i].ObtenerApellido()} no tuvo movimientos")