from CLASEGESTOR import gestor

if __name__ == "__main__":
    ContenedorVehiculos = gestor()
    opcion = int(input("Ingrese opcion: \n 1) Agregar Vehículos \n 2) Mostrar tipo de vehículo \n 3) Mostrar Cantidad de Autobuses y Vanes \n 4) Mostrar Vehículos \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
            ContenedorVehiculos.CargaVehiculos()
        if opcion == 2:
            ContenedorVehiculos.BuscarVehiculo()
        if opcion == 3:
            ContenedorVehiculos.ContarAyV()
        if opcion == 4:
            ContenedorVehiculos.MostrarVehiculos()
        opcion = int(input("Ingrese opcion: \n 1) Agregar Vehículos \n 2) Mostrar tipo de vehículo \n 3) Mostrar Cantidad de Autobuses y Vanes \n 4) Mostrar Vehículos \n >>INGRESE 0 PARA FINALIZAR<<\n"))