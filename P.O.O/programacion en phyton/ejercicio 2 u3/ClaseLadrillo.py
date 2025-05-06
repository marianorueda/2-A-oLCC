class Ladrillo:
    __alto : int
    __largo : int
    __ancho : int
    __cantidad : int
    __id : int
    __kgMatPrimUti : float
    __costo : float
    __materiales : list
    def __init__(self, alto, largo, ancho, cantidad, id, kgMatPrimUti, costo, material):
        self.__alto = alto
        self.__largo = largo
        self.__ancho = ancho
        self.__cantidad = cantidad
        self.__id = id
        self.__kgMatPrimUti = kgMatPrimUti
        self.__costo = costo
        if material != None:
            self.addMaterial(material, 1)

    def getAlto(self):
        return self.__alto

    def getLargo(self):
        return self.__largo

    def getAncho(self):
        return self.__ancho

    def getCantidad(self):
        return self.__cantidad

    def getId(self):
        return self.__id

    def getKgMatPrimUti(self):
        return self.__kgMatPrimUti

    def getCosto(self):
        return self.__costo