from GestorCabanaJOSE import gestorcabana
from GestorReservaJOSE import gestorreserva

if __name__ == "__main__":
    print("Menu de opciones:")
    cabana = gestorcabana()
    reserva = gestorreserva()
    a = int(input(
        " 1. Mostrar Cabañas habilitadas \n 2. Emitir Listado \n 0. Para finalizar \n Su opcion: "))
    while a != 0:
        if a == 1:
            cant = int(input("Ingrese cantidad de huespedes: "))
            cabana.Mostrar(cant, reserva)
        a = int(input(
            " 1. Mostrar Cabañas habilitadas \n 2. Emitir Listado \n 0. Para finalizar \n Su opcion: "))
