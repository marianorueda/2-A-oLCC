class publicacion:
    __titulo : str
    __categoria : str
    __precio : float
    def __init__(self, titulo, categoria, precio):
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio = precio
    def getTitulo(self):
        return self.__titulo
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def __str__(self):
        return(f"{self.__titulo}, {self.__categoria}, {self.__precio}")
    def calcularImporte(self):
        pass