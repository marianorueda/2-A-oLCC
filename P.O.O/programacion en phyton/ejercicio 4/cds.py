from publicaciones import publicacion
class cd(publicacion):
    __tiempo : str
    __nombre : str
    def __init__(self, titulo, categoria, precio, tiempo, nombre):
        super().__init__(titulo, categoria, precio)
        self.__tiempo = tiempo
        self.__nombre = nombre
    def getTiempo(self):
        return self.__tiempo
    def getNombre(self):
        return self.__nombre
    def __str__(self):
        return (f"Tiempo: {self.__tiempo}, Nombre: {self.__nombre}, Título: {self.getTitulo()}, Categoría: {self.getCategoria()}, Precio: {self.getPrecio()}")
    def CalcularImporte(self):
        return float(self.getPrecio()*1.1)