from CLASEGESTOR import gestor

if __name__ == "__main__":
    ContenedorPlanes = gestor()
    ContenedorPlanes.CargarPlanes()
    opcion = int(input("Ingrese opcion: \n 1) Consultar tipo de plan \n 2) Contar planes por zona geográfica \n 3) Buscar planes con un numero de canales internacionales \n 4) Mostrar Planes \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
            try:
                pos = int(input("Ingrese la posicion del plan a consultar"))
                ContenedorPlanes.MostrarTipoPlan(pos)
            except ValueError:
                print("La posicion ingresada debe ser un numero")
            except IndexError:
                print("La posicion ingresada no existe")
        if opcion == 2:
            zona = input("Ingrese la zona geográfica")
            ContenedorPlanes.ContarPlanes(zona)
        if opcion == 3:
            cant = int(input("Ingrese el numero de canales internacionales que desea"))
            ContenedorPlanes.BuscarPlanesInternacionales(cant)
        if opcion == 4:
            ContenedorPlanes.MostrarPlanes()
        opcion = int(input("Ingrese opcion: \n 1) Consultar tipo de plan \n 2) Contar planes por zona geográfica \n 3) Buscar planes con un numero de canales internacionales \n 4) Mostrar Planes \n >>INGRESE 0 PARA FINALIZAR<<\n")) 