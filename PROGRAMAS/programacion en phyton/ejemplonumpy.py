import numpy as np

# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

# Función para ingresar datos de una persona
def ingresar_persona():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    ocupacion = input("Ingrese la ocupación de la persona: ")
    return Persona(nombre, edad, ocupacion)

# Función de prueba
def test():
    # Creación de un arreglo NumPy vacío para almacenar personas
    personas_array = np.empty(0, dtype=[("nombre", "U20"), ("edad", int), ("ocupacion", "U20")])

    # Ingresar datos de personas
    num_personas = int(input("Ingrese el número de personas a registrar: "))
    for _ in range(num_personas):
        persona = ingresar_persona()
        personas_array = np.append(personas_array, persona)

    # Ordenación por edad (de menor a mayor)
    sorted_by_age = np.sort(personas_array, order="edad")
    print("\nOrdenado por edad:")
    for persona in sorted_by_age:
        print(f"{persona['nombre']} ({persona['edad']} años)")

    # Búsqueda de personas mayores de 25 años
    mayores_25 = personas_array[personas_array["edad"] > 25]
    print("\nPersonas mayores de 25 años:")
    for persona in mayores_25:
        print(f"{persona['nombre']} ({persona['ocupacion']})")

# Ejecutar la función de prueba
test()
