from ejercicio3 import gestor

if __name__ == '__main__':
    Gestor = gestor()
    opcion = int(input("Ingrese opcion:\n 1_Cargar facturacion\n 2_Calcular facturacion total para una sucursal\n 3_Ingresar un día y obtener sucursal que más facturo\n 4_Calcular sucursal con menos facturacion durante la semana\n 5_Calcular total de todas las sucursales 0_Para finalizar\n"))
    while opcion != 0:
        if opcion == 1:
            Gestor.CargarDatos()
        if opcion == 2:
            Gestor.CalcularFacturacion()
        if opcion == 3:
            Gestor.MayoresVentas()
        if opcion == 4:
            Gestor.MenoresVentas()
        if opcion == 5:
            Gestor.TotalSemanal()
        opcion = int(input("Ingrese opcion:\n 1_Cargar facturacion\n 2_Calcular facturacion total para una sucursal\n 3_Ingresar un día y obtener sucursal que más facturo\n 4_Calcular sucursal con menos facturacion durante la semana\n 5_Calcular total de todas las sucursales 0_Para finalizar\n"))



