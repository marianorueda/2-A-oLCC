from publicaciones import publicacion
class libro(publicacion):
    __nombre : str
    __fecha : str
    __pags : int
    def __init__(self, titulo, categoria, precio, nombre, fecha, pags):
        super().__init__(titulo, categoria, precio)
        self.__nombre = nombre
        self.__fecha = fecha
        self.__pags = pags
    def getNombre(self):
        return self.__nombre
    def getFecha(self):
        return self.__fecha
    def getPags(self):
        return self.__pags
    def __str__(self):
        return f"Nombre del Narrador: {self.__nombre}, Fecha: {self.__fecha}, Numero de Páginas: {self.__pags}, Título: {self.getTitulo()}, Categoría: {self.getCategoria()}, Precio: {self.getPrecio()}"
    def calcularImporte(self):
        diferencia = 2024 - self.getFecha()
        return float((diferencia/100)*self.getPrecio())