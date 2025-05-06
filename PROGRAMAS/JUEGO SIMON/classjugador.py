class jugador:
    __nombre:str
    __puntos:int
    __fecha:str
    __hora:str
    def __init__(self,nom,pun,fec,hor):
        self.__nombre=nom
        self.__fecha=fec
        self.__hora=hor
        self.__puntos=pun
    def mostrar(self):
        print("____________________")
        print(f"nombre:{self.__nombre}, fecha:{self.__fecha}, hora:{self.__hora} puntos:{self.__puntos}")
    def getnombre(self):
        return self.__nombre
    def getfecha(self):
        return self.__fecha
    def gethora(self):
        return self.__hora
    def getpuntos(self):
        return self.__puntos
    def __gt__(self, otro):
        return self.__puntos > otro.__puntos