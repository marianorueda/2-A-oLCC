from CLASEGESTORDEEQUIPOS import GestoreDeEquipos

if __name__ == "__main__":
    gestor = GestoreDeEquipos()
    gestor.cargarEquipos()
    opcion = int(input("Ingrese la opcion deseada: \n 1. Consultar tipo de equipo \n 2. Buscar herramientas electricas por año de fabricacion \n 3. Mostrar Maquinarias Pesadas con una capacidad de carga menor o igual a una ingresada \n 4. Mostrar todos los equipos \n  ---INGRESE 0 PARA SALIR--- \n"))
    while (opcion != 0):
        if opcion == 1:
            try:
                pos = int(input("Ingrese la posicion del equipo deseada: \n"))
                gestor.mostrarTipoPlan(pos)
            except ValueError:
                print("La posicion debe se un numero entero")
            except IndexError as mensaje:
                print(mensaje)
        elif opcion == 2:
            ano = int(input("Ingrese el año de fabricacion del equipo deseado: \n"))
            gestor.contarHerramientasElectricas(ano)
        elif opcion == 3:
            capacidad = float(input("Ingrese capacidad: \n"))
            gestor.contarEquiposConCapacidadCarga(capacidad)
        elif opcion == 4:  
            gestor.mostrarEquipos()
        opcion = int(input("Ingrese la opcion deseada: \n 1. Consultar tipo de equipo \n 2. Buscar herramientas electricas por año de fabricacion \n 3. Mostrar Maquinarias Pesadas con una capacidad de carga menor o igual a una ingresada \n 4. Mostrar todos los equipos \n  ---INGRESE 0 PARA SALIR--- \n"))