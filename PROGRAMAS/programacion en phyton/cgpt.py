import csv
import numpy as np

class Cliente:
    def __init__(self, nombre, apellido, dni, num_cuenta, saldo_anterior):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.num_cuenta = num_cuenta
        self.saldo_anterior = saldo_anterior
    
    def __str__(self):
        return f"{self.apellido} {self.nombre}"

class Movimiento:
    def __init__(self, num_cuenta, fecha, descripcion, tipo, importe):
        self.num_cuenta = num_cuenta
        self.fecha = fecha
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
    
    def __str__(self):
        return f"{self.fecha} {self.descripcion} {self.importe} {self.tipo}"

class GestorClientes:
    def __init__(self):
        self.clientes = []
    
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def buscar_cliente_por_dni(self, dni):
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

class GestorMovimientos:
    def __init__(self):
        self.movimientos = np.array([])
    
    def agregar_movimiento(self, movimiento):
        self.movimientos = np.append(self.movimientos, movimiento)
    
    def ordenar_por_numero_de_cuenta(self):
        self.movimientos = sorted(self.movimientos, key=lambda x: x.num_cuenta)
    
    def buscar_movimientos_por_numero_de_cuenta(self, num_cuenta):
        return [movimiento for movimiento in self.movimientos if movimiento.num_cuenta == num_cuenta]

# Funciones para cargar datos desde archivos CSV
def cargar_clientes(gestor_clientes, archivo):
    with open("ClientesFarmaCiudad,csv", 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Ignorar la fila de encabezado
        for row in reader:
            cliente = Cliente(row[0], row[1], row[2], row[3], float(row[4]))
            gestor_clientes.agregar_cliente(cliente)

def cargar_movimientos(gestor_movimientos, archivo):
    with open("MovimientosAbril2024,csv", 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) 
        for row in reader:
            movimiento = Movimiento(row[0], row[1], row[2], row[3], float(row[4]))
            gestor_movimientos.agregar_movimiento(movimiento)


def actualizar_saldo(gestor_clientes, gestor_movimientos):
    dni = input("Ingrese el DNI del cliente: ")
    cliente = gestor_clientes.buscar_cliente_por_dni(dni)
    if cliente:
        movimientos = gestor_movimientos.buscar_movimientos_por_numero_de_cuenta(cliente.num_cuenta)
        saldo_actual = cliente.saldo_anterior
        print(f"Cliente: {cliente}, Número de Cuenta: {cliente.num_cuenta}")
        print(f"Saldo anterior: {saldo_actual}")
        print("Movimientos")
        print("Fecha    Descripción    Importe    Tipo de movimiento")
        for movimiento in movimientos:
            print(movimiento)
            if movimiento.tipo == 'C':
                saldo_actual += movimiento.importe
            elif movimiento.tipo == 'P':
                saldo_actual -= movimiento.importe
        print(f"Saldo actualizado: {saldo_actual}")
    else:
        print("Cliente no encontrado.")

def cliente_sin_movimientos(gestor_clientes, gestor_movimientos):
    dni = input("Ingrese el DNI del cliente: ")
    cliente = gestor_clientes.buscar_cliente_por_dni(dni)
    if cliente:
        movimientos = gestor_movimientos.buscar_movimientos_por_numero_de_cuenta(cliente.num_cuenta)
        if not movimientos:
            print(f"{cliente.apellido} {cliente.nombre} no tuvo movimientos en abril 2024.")
        else:
            print(f"{cliente.apellido} {cliente.nombre} sí tuvo movimientos en abril 2024.")
    else:
        print("Cliente no encontrado.")

# Carga de datos desde archivos CSV
gestor_clientes = GestorClientes()
cargar_clientes(gestor_clientes, "ClientesFarmaCiudad.csv")

gestor_movimientos = GestorMovimientos()
cargar_movimientos(gestor_movimientos, "MovimientosAbril2024.csv")

# Menú de opciones
while True:
    print("\nMenú de opciones:")
    print("1. Actualizar saldo de un cliente.")
    print("2. Verificar si un cliente tuvo movimientos en abril 2024.")
    print("3. Salir.")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        actualizar_saldo(gestor_clientes, gestor_movimientos)
    elif opcion == "2":
        cliente_sin_movimientos(gestor_clientes, gestor_movimientos)
    elif opcion == "3":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
