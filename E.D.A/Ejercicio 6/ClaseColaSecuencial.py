from random import uniform
import numpy as np

class Cliente:
    __tiempoEjec : int
    __tiempoEspera : int

    def __init__(self, tiempoEjec):
        self.__tiempoEjec = tiempoEjec
        self.__tiempoEspera = 0

    def getTiempoEjec(self):
        return self.__tiempoEjec
    
    def setTiempoEjec(self):
        self.__tiempoEjec -= 1

    def __str__(self):
        return f"Cliente"
    
    def setTiempoEspera(self, sum):
        self.__tiempoEspera = int(sum)

    def getTiempoEspera(self):
        return self.__tiempoEspera

class ColaSecuencial:
    __ult : int
    __pri : int
    __cont : int
    __arregloDatos : np.ndarray

    def __init__(self):
        self.__pri = 0
        self.__ult = 0
        self.__cont = 0
        self.__arregloDatos = np.empty(5,dtype = Cliente)

    def getCont(self):
        return self.__cont

    def vacia(self):
        return self.__cont == 0

    def llena(self):
        return self.__cont == len(self.__arregloDatos)

    def insertar(self,item):
        if self.__cont < len(self.__arregloDatos):
            cliente = Cliente(item)
            self.__arregloDatos[self.__ult] = cliente
            self.__ult = (self.__ult+1) % len(self.__arregloDatos)
            self.__cont += 1
            sum = self.calcularTiempoEspera()
            self.__arregloDatos[self.__ult-1].setTiempoEspera(sum)
        else:
            print(f"No es posible insertar el elemento {item}. Pila llena")


    def suprimir(self):
        elemento = None
        if self.vacia() is False:
            elemento = self.__arregloDatos[self.__pri]
            self.__pri  = (self.__pri+1) % len(self.__arregloDatos)
            self.__cont -= 1
        else:
            print("No es posible eliminar elementos. La pila esta vacia")
        return elemento

    def recorrer(self):
        i = self.__pri
        if self.vacia() is False:
            for j in range(self.__cont):
                print(self.__arregloDatos[i])
                i = (i + 1) % len(self.__arregloDatos)
    
    def llega_cliente(self):
        random = uniform(0,1) # Determina si llega impresion
        if random <= 1/2: #La formula es 1/Frecuencia ; Siendo en este caso 5.
            llego_cliente = True
        else:
            llego_cliente = False
        return llego_cliente
        
    def minuto(self):
        band = False
        if not self.vacia():
            if self.__arregloDatos[self.__pri].getTiempoEjec() > 1:
                self.__arregloDatos[self.__pri].setTiempoEjec()
            else: 
                self.suprimir()
                band = True
        return band

    def calcularTiempoEspera(self):
        sum = 0
        if not self.vacia():
            for i in range(self.__cont):
                sum += self.__arregloDatos[i].getTiempoEjec()
        return sum
        
    def getTiempoEsperaUltimo(self):
        return self.__arregloDatos[self.__ult-1].getTiempoEspera()
            
if __name__ == "__main__":
    c1 = ColaSecuencial()
    c2 = ColaSecuencial()
    c3 = ColaSecuencial()
    tiempo = 0
    maximo = 0
    cont1 = 0
    cont2 = 0
    sum = 0
    
    while tiempo < 120: 
        print(f"---- Tiempo: {tiempo} -----")
        if c1.llega_cliente():
            cont1 += 1
            if c1.vacia():
                c1.insertar(5)
                print("Se ha insertado el cliente en la cola 1, está siendo atendido")
            elif c2.vacia():
                c2.insertar(3)
                print("Se ha insertado el cliente en la cola 2, está siendo atendido") 
            elif c3.vacia():
                c3.insertar(4)
                print("Se ha insertado el cliente en la cola 3, está siendo atendido")
            else:
                if c1.getCont() <= c2.getCont() and c1.getCont() <= c3.getCont():
                    sum += c1.calcularTiempoEspera()
                    c1.insertar(5)
                    if c1.getTiempoEsperaUltimo() > maximo:
                        maximo = c1.getTiempoEsperaUltimo()
                    print("Se ha insertado el cliente en la cola 1, está esperando ser atendido")
                elif c2.getCont() <= c1.getCont() and c2.getCont() <= c3.getCont():
                    sum += c2.calcularTiempoEspera()
                    c2.insertar(3)
                    if c1.getTiempoEsperaUltimo() > maximo:
                        maximo = c2.getTiempoEsperaUltimo()
                    print("Se ha insertado el cliente en la cola 2, está esperando ser atendido")
                elif c3.getCont() <= c1.getCont() and c3.getCont() <= c2.getCont():
                    sum += c3.calcularTiempoEspera()
                    c3.insertar(4)
                    if c1.getTiempoEsperaUltimo() > maximo:
                        maximo = c3.getTiempoEsperaUltimo()
                    print("Se ha insertado el cliente en la cola 3, está esperando ser atendido")
        tiempo += 1
        if c1.minuto():
            print("El cliente de la cola 1 fue atendido")
            cont2 += 1
        if c2.minuto():
            print("El cliente de la cola 2 fue atendido")
            cont2 += 1
        if c3.minuto():
            print("El cliente de la cola 3 fue atendido")
            cont2 += 1
    print(f"El numero de clientes atendidos es {cont2}")
    sinAtender = cont1 - cont2
    prom = sum / cont2
    print(f"El promedio de tiempo de espera es de {prom} minutos para los clientes atendidos")
    prom = sum / cont1
    print(f"El promedio de tiempo de espera es de {prom} minutos para los clientes sin atender")
    print(f"El numero de clientes sin atender es {sinAtender}")
    print(f"El maximo tiempo de espera es de {maximo} minutos")
    print ("La cola 1 quedo:")
    c1.recorrer()
    print ("La cola 2 quedo:")
    c2.recorrer()
    print ("La cola 3 quedo:")
    c3.recorrer()
        

