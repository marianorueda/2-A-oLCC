from ClaseColeccion import Coleccion
from ClaseClienteLocal import ClienteLocal
from ClaseClienteNacional import ClienteNacional

if __name__ == "__main__":
    coleccion = Coleccion()
    coleccion.insertarAlFinal(ClienteLocal("Julian", "Alvarez", "julianalvarez@gmail.com", "123456", "Av. Rawson, 1234", "54321"))
    coleccion.insertarAlFinal(ClienteLocal("Pedro", "Calani", "pedrocalani@gmail.com", "123456", "Av. Libertador, 1234", "54321"))
    coleccion.insertarAlFinal(ClienteNacional("Carlos", "Tapia", "carlostapia@gmail.com", "123456", "Av. Ignacio de la Roza, 1234", "54321", "Buenos Aires", "La Plata", "12345"))
    coleccion.insertarAlFinal(ClienteNacional("Luis", "Rueda", "luisrueda@gmail.com", "123456", "Av. 25 de Mayo, 1234", "54321", "San Juan", "Rawson", "12345"))
    coleccion.mostrar()
    opcion = input("Ingrese la opcion deseada: \n 1. Insertar cliente al final de la lista \n 2.Mostrar clientes nacionales \n 3. Buscar cliente por posicion \n 4. Salir \n")
    while opcion != "4":
        if opcion == "1":
            tipo = int(input("Ingrese el tipo de cliente deseado: \n 1. Local \n 2. Nacional \n"))
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            email = input("Ingrese el email del cliente: ")
            contrasena = input("Ingrese la contraseña del cliente: ")
            direccion = input("Ingrese la direccion del cliente: ")
            telefono = input("Ingrese el telefono del cliente: ")
            if tipo == 1:
                coleccion.insertarAlFinal(ClienteLocal(nombre, apellido, email, contrasena, direccion, telefono))
            elif tipo == 2:
                provincia = input("Ingrese la provincia del cliente: ")
                localidad = input("Ingrese la localidad del cliente: ")
                codigoPostal = input("Ingrese el codigo postal del cliente: ")
                coleccion.insertarAlFinal(ClienteNacional(nombre, apellido, email, contrasena, direccion, telefono, provincia, localidad, codigoPostal))
            else:
                print("Opcion invalida")
            coleccion.mostrar()
        elif opcion == "2":
            coleccion.mostrarClientesNacionales()
        elif opcion == "3":
            pos = int(input("Ingrese la posicion deseada: "))
            coleccion.buscarPosicion(pos)
        opcion = input("Ingrese la opcion deseada: \n 1. Insertar cliente al final de la lista \n 2.Mostrar clientes nacionales \n 3. Buscar cliente por posicion \n 4. Salir \n")

