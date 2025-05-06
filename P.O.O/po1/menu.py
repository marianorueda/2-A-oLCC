from Movimientos import GestorMovimientos
from Clientes import GestorClientes

def DesplegarMenu():
    ContenedorClientes = GestorClientes()
    ContenedorMovimientos = GestorMovimientos()
    opcion = int(input("Ingrese opcion:\n 1) Actualizar Saldo \n 2) Informe Cliente \n 3) Ordenar Movimientos \n Ingrese 0 para finalizar \n"))
    while opcion != 0:
        if opcion == 1:
            dni = int(input("Ingrese dni del cliente: "))
            i = ContenedorClientes.BuscarCliente(dni)
            if i!=-1:
                ContenedorClientes.ActualizarCliente(i, ContenedorMovimientos)
            else:
                print("El dni ingresado no pertenece a un cliente")
        elif opcion == 2:
            dni = int(input("Ingrese dni del cliente: "))
            i = ContenedorClientes.BuscarCliente(dni)
            if i!=-1:
                ContenedorClientes.InformeCliente(i, ContenedorMovimientos)
            else:
                print("El dni ingresado no pertenece a un cliente")
        elif opcion == 3:
            ContenedorMovimientos.OrdenarMovimientos()
        opcion = int(input("Ingrese opcion:\n 1) Actualizar Saldo \n 2) Informe Cliente \n 3) Ordenar Movimientos \n Ingrese 0 para finalizar \n"))

if __name__== '__main__':
    DesplegarMenu()
