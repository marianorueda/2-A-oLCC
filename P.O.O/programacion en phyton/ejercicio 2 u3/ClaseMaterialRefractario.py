class MaterialRefractario:
    __material : str
    __caracteristicas : str
    __cantUtilizada : float
    __costoAdicional : float
    def __init__(self, material, caracteristicas, cantUtilizada, costoAdicional):
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cantUtilizada = cantUtilizada
        self.__costoAdicional = costoAdicional