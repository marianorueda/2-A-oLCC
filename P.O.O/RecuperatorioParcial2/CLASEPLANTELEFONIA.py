from CLASEPLANES import plan
class ptelefonia(plan):
    __tipo : str
    __tiempo : int
    def __init__(self, nombre, duracion, cobertura, precio, tipo, tiempo):
        super().__init__(nombre, duracion, cobertura, precio)
        self.__tipo = tipo
        self.__tiempo = tiempo
    def CalcularImporte(self):
        if (self.__tipo == "internacional"):
            return (self.ObtenerPrecio()*1.2)
        elif(self.__tipo == "locales")or(self.__tipo == "larga distancia"):
            return (self.ObtenerPrecio()*0.925)