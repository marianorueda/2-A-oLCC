from CLASEPLANES import plan
class ptelevision(plan):
    __cnacionales : int
    __cinternacionales : int
    def __init__(self, nombre, duracion, cobertura, precio, cnacionales, cinternacionales):
        super().__init__(nombre, duracion, cobertura, precio)
        self.__cnacionales = cnacionales
        self.__cinternacionales = cinternacionales
    def ObtenerCantInter(self):
        return self.__cinternacionales
    def CalcularImporte(self):
        if (self.__cinternacionales > 10):
            return (self.ObtenerPrecio()*1.15)
        else:
            return self.ObtenerPrecio()
    