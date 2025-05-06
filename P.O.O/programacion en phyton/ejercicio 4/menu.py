from gestorpublicaciones import gestor

if __name__ == "__main__":
    ContenedorPublicaciones = gestor()
    opcion = int(input("Ingrese opcion: \n 1) Agregar Publicaciones \n 2) Mostrar tipo de publicacion \n 3) Mostrar Cantidad de Libros y de CDs \n 4) Mostrar Publicaciones \n >>INGRESE 0 PARA FINALIZAR<<\n"))
    while opcion != 0:
        if opcion == 1:
           ContenedorPublicaciones.agregarCds()
           ContenedorPublicaciones.agregarLibros()
        if opcion == 2:
            pos = int(input("Ingrese la posicion de la publicacion en la lista"))
            ContenedorPublicaciones.buscarTipo(pos)
        if opcion == 3:
            ContenedorPublicaciones.contarPublicaciones()
        if opcion == 4:
            ContenedorPublicaciones.mostrar()
        opcion = int(input("Ingrese opcion: \n 1) Agregar Publicaciones \n 2) Mostrar tipo de publicacion \n 3) Mostrar Cantidad de Libros y de CDs \n 4) Mostrar Publicaciones \n >>INGRESE 0 PARA FINALIZAR<<\n"))