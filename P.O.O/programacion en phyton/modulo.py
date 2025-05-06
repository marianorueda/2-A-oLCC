from clases import cajadeahorro
class contenedor:
    __cuentas: list
    def __init__(self):
        self.__cuentas=[]
    def agregar(self, unObjeto: cajadeahorro):
        self.__cuentas.append(unObjeto)
    def unaCuenta_obtenerCuil(self, cuil, j):
        cuil=self.__cuentas[j].__cuil
    def unaCuenta_obtenerNombre(self, j):
        return self.__cuentas[j].__nombre
    def unaCuenta_obtenerApellido(self, j):
        return self.__cuentas[j].__apellido
    def unaCuenta_obtenerSaldo(self, j):
        return self.__cuentas[j].__saldo



if __name__=="__main__":
    prueba=cajadeahorro("","","","",0)
    prueba.test2()
    contenedor=contenedor()
    for i in range(1):
        contenedor.agregar(prueba)
    cuil=input("Ingrese cuil a buscar:")
    j=0
    xcuil=prueba.getCuil()
    while cuil!=xcuil:
        xcuil=prueba.getCuil()
        j+1
    print("Los datos de la cuenta son: {}, {}, {}", contenedor.unaCuenta_obtenerNombre(j), contenedor.unaCuenta_obtenerApellido(j), contenedor.unaCuenta_obtenerSaldo(j))






