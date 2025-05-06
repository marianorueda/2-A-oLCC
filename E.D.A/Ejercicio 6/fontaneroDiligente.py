"""   def fontaneroDiligente(tiemposReparacion):
    # Ordenar los tiempos de reparación en orden ascendente
    tiemposOrdenados = sorted(tiemposReparacion)
    
    # Inicializar variables para el tiempo de espera total y el tiempo acumulado
    tiempoTotalEspera = 0
    tiempoAcumulado = 0
    
    # Recorrer los tiempos de reparación ya ordenados
    for tiempo in tiemposOrdenados:
        # Incrementar el tiempo acumulado con el tiempo de la tarea actual
        tiempoAcumulado += tiempo
        # Sumar el tiempo acumulado al tiempo total de espera
        tiempoTotalEspera += tiempoAcumulado

    return tiempoTotalEspera, tiemposOrdenados

# Ejemplo de tiempos de reparación
tiemposReparacion = [3, 1, 4, 3, 2]

# Calcular la solución óptima
tiempoTotal, orden_optimo = fontaneroDiligente(tiemposReparacion)

# Imprimir el resultado
print("Orden óptimo de reparación:", orden_optimo)
print("Tiempo total de espera:", tiempoTotal) """
      
      
class fontaneroDiligente:
    __arreglo : []
    def __init__(self, arreglo):
        self.__arreglo = arreglo
    def ordenarOptimo(self):
        tiemposOrdenados = sorted(self.__arreglo)  # Ordenar los tiempos de reparación en orden ascendente
        self.__arreglo = tiemposOrdenados
    def tiempoTotalEspera(self):
        tiempoTotalEspera = 0
        tiempoAcumulado = 0
        for tiempo in self.__arreglo:
            tiempoAcumulado += tiempo
            tiempoTotalEspera += tiempoAcumulado