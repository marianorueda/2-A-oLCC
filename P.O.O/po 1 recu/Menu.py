from GestorMamas import gestorMamas
from GestorNacimientos import gestorNacimientos

if __name__ == "__main__":
    ContenedorMamas = gestorMamas()
    ContenedorNacimientos = gestorNacimientos()
    opcion = int(input("Ingrese opcion: \n 1) Informe Mamá \n 2) Informar Madres con parto múltiple \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
            dni = int(input("Ingrese DNI de la Mamá \n"))
            ContenedorMamas.BuscarMama(dni, ContenedorNacimientos)
        if opcion == 2:
            ContenedorMamas.BuscarPartosMultiples(ContenedorNacimientos)
        opcion = int(input("Ingrese opcion: \n 1) Informe Mamá \n 2) Informar Madres con parto múltiple \n >>INGRESE 0 PARA FINALIZAR<<\n"))