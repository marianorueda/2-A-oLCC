from ClaseGestorConexiones import GestorConexiones
from ClaseGestorGammer import GestorGammer

if __name__ == "__main__":
    ContenedorGammer = GestorGammer()
    ContenedorConexiones = GestorConexiones()
    ContenedorGammer.CargarGammers()
    opcion = int(input("Ingrese opcion: \n 1) Informar conexiones para un dni \n 2) Jugadores de cierto jugo \n 3) Consultar conexiones simultáneas servicio basico \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
            dni = int(input("Ingrese DNI del jugador \n"))
            ContenedorGammer.BuscarGammer(dni, ContenedorConexiones)
        if opcion == 2:
            juego = input("Ingrese el nombre del juego \n")
            ContenedorConexiones.ConexionesJuego(juego, ContenedorGammer)
        opcion = int(input("Ingrese opcion: \n 1) Informar conexiones para un dni \n 2) Jugadores de cierto jugo \n 3) Consultar conexiones simultáneas servicio basico \n >>INGRESE 0 PARA FINALIZAR<<\n"))