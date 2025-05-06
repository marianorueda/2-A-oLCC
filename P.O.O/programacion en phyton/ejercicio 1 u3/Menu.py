from ClaseGestorEdificios import GestorEdificios

if __name__ == "__main__":
    ContenedorEdificios = GestorEdificios()
    opcion = int(input("Ingrese opcion: \n 1) Mostrar Propietarios \n 2) Mostrar superficie total de un edificio \n 3) Mostrar Departamento \n 4) Mostrar cantidad de departamentos con 3 dormitorios y mas de 1 baño \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
            idEdificio = int(input("Ingrese el id del edificio \n"))
            ContenedorEdificios.mostrarPropietarios(idEdificio)
        elif opcion == 2:
            nomEdificio = input("Ingrese el nombre del edificio \n")
            ContenedorEdificios.buscarSuperficie(nomEdificio)
        elif opcion == 3:
            nomPropietario = input("Ingrese el nombre del propietario \n")
            ContenedorEdificios.deptosSuperficie(nomPropietario)
        elif opcion == 4:
            numPiso = int(input("Ingrese el numero de piso \n"))
            ContenedorEdificios.buscarDepartamentos(numPiso)
        opcion = int(input("Ingrese opcion: \n 1) Mostrar Propietarios \n 2) Mostrar superficie total de un edificio \n 3) Mostrar Departamento \n 4) Mostrar cantidad de departamentos con 3 dormitorios y mas de 1 baño \n >>INGRESE 0 PARA FINALIZAR<<\n"))