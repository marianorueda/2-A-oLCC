from ClaseColaSecuencial import ColaSecuencial
from ClaseSolicitante import Solicitante

if __name__ == "__main__":
    cola = ColaSecuencial()
    reloj = 0
    while reloj < 300:
        if cola.llegaCliente():
            if cola.vacia():
                solicitante = Solicitante()
                cola.insertar(solicitante)
            else:
                solicitante = Solicitante()
                solicitante.setTiempoEspera(cola.calcularTiempoEspera())
                cola.insertar(solicitante)
        reloj += 1
        cola.tiempo()