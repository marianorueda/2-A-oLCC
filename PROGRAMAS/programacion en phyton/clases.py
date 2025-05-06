class cajadeahorro:
    __nroCuenta: str
    __cuil: str
    __apellido: str
    __nombre: str
    __saldo: float
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta=nroCuenta
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo=float(saldo)
    def mostrarDatos(self):
        print("numero de cuenta:", self.__nroCuenta)
        print("cuil:", self.__cuil)
        print("apellido:", self.__apellido)
        print("nombre:", self.__nombre)
        print("saldo:", self.__saldo)
    def extraer(self, importe):
        if self.__saldo>=importe:
            self.__saldo-=importe
            print("el nuevo saldo es:", self.__saldo)
        else:
            print("Saldo insuficiente")
            return -1
    def depositar(self, importe):
        if importe>0:
            self.__saldo+=importe
    def validar_cuil(self):
        return 1
    def CompararCuil(self, cuil):
        while cuil!=self.__cuil:
            
    def test(self):
        for i in range(3):
            print("Ingrese los datos de su cuenta:")
            nroCuenta=input("Numero de cuenta:")
            cuil=input("cuil:")
            apellido=input("apellido:")
            nombre=input("nombre:")
            saldo=float(input("saldo:"))
            persona=cajadeahorro(nroCuenta, cuil, apellido, nombre, saldo)
            importe=float(input("Ingrese importe de extraccion:"))
            persona.extraer(importe)
            importe2=float(input("Ingrese importe de depósito:"))
            persona.depositar(importe2)
            persona.validar_cuil()
            persona.mostrarDatos()
    def test2(self):
        for i in range(1):
            print("Ingrese los datos de su cuenta:")
            nroCuenta=input("Numero de cuenta:")
            cuil=input("cuil:")
            apellido=input("apellido:")
            nombre=input("nombre:")
            saldo=float(input("saldo:"))
            persona=cajadeahorro(nroCuenta, cuil, apellido, nombre, saldo)