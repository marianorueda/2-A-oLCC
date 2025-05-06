import numpy as np

class Secuencial:
    __numVertices: int
    __matriz: np.ndarray
    
    def __init__(self, numVertices):
        self.__numVertices = numVertices
        self.__matriz = np.zeros((numVertices, numVertices))
        
    def agregarArista(self, origen, destino, peso=1):
        if origen >= self.__numVertices or destino >= self.__numVertices:
            raise ValueError("El origen o el destino no es válido")
        self.__matriz[origen, destino] = peso

        
    def mostrar(self):
        for fila in self.__matriz:
            print(fila)
            
    def adyacentes(self, nodo):
        if nodo >= self.__numVertices:
            raise ValueError("nodo fuera de rango")
        else:
            adyacentes = []
            for i in range(self.__numVertices):
                if self.__matriz[nodo, i] != 0 and self.__matriz[i,nodo] != 0:
                    adyacentes.append(i)
            if len(adyacentes) > 0:
                for j in range(len(adyacentes)):
                    print(f"Nodo {nodo} tiene un adyacente {adyacentes[j]}")
            else:
                print(f"Nodo {nodo} no tiene adyacentes")
                
    def gradoSalida(self, nodo): #cantidad de aristas que salen de un nodo
        if nodo >= self.__numVertices:
            raise ValueError("nodo fuera de rango")
        else:
            grado = 0
            for i in range(self.__numVertices):
                if self.__matriz[nodo][i]==1:
                    grado += 1
            print(f"el grado de salida del nodo {nodo} es {grado}")
            return grado
        
    def gradoEntrada(self, nodo): #cantidad de aristas que entran en un nodo
        if nodo >= self.__numVertices:
            raise ValueError("nodo fuera de rango")
        else:
            grado = 0
            for i in range(self.__numVertices):
                if self.__matriz[i][nodo]==1:
                    grado += 1
            print(f"el grado de entrada del nodo {nodo} es {grado}")
            return grado
        
    def nodoFuente(self, nodo): #no tiene aristas entrantes
        if self.gradoEntrada(nodo) == 0 and self.gradoSalida(nodo) > 0:
            print(f"nodo {nodo} es fuente")
            return True
        else:
            print(f"nodo {nodo} no es fuente")
            return False

    def nodosFuentes(self):
        c = 0
        for i in range(self.__numVertices):
            if self.nodoFuente(i):
                c += 1
        return c

    def nodoSumidero(self, nodo): #no tiene aristas salientes
        if self.gradoSalida(nodo) == 0 and self.gradoEntrada(nodo) > 0:
            print(f"nodo {nodo} es sumidero")
            return True
        else:
            print(f"nodo {nodo} no es sumidero")
            return False

            
    def camino(self, inicio, fin):
        if inicio >= self.__numVertices or fin >= self.__numVertices:
            raise ValueError("El origen o el destino no es válido")
        else:
            visitados = [False] * self.__numVertices #crea una lista con la cantidad de vertices en false
            pila = [(inicio, [inicio])] #pila que contiene el nodo actual y el camino hasta el nodo actual
            
            while pila:
                nodoActual, caminoActual = pila.pop()
                print(f"camino {caminoActual} del nodo actual {nodoActual}")
                if nodoActual == fin:
                    return caminoActual
                
                if not visitados[nodoActual]:
                    visitados[nodoActual] = True
                    
                    for i in range(self.__numVertices):
                        if self.__matriz[nodoActual] [i] == 1 and not visitados[i]:
                            pila.append((i, caminoActual + [i]))
                            
                            
    def conexo(self): #profundidad
        visitados = [False] * self.__numVertices
        pila = [0]
        
        while pila:
            vertice = pila.pop() #amplitud es popleft
            if not visitados[vertice]:
                visitados[vertice] = True
                for i in range(self.__numVertices):
                    if self.__matriz[vertice][i] == 1 and not visitados[i]:
                        pila.append(i)
        return all(visitados)

    def aciclico(self):
        visitados = [False] * self.__numVertices
        pila = [(0, -1)]

        while pila:
            nodoActual, padre = pila.pop()
            if not visitados[nodoActual]:
                visitados[nodoActual] = True
                for i in range(self.__numVertices):
                    if self.__matriz[nodoActual][i] == 1 and not visitados[i]:
                        pila.append((i, nodoActual))
                    elif self.__matriz[nodoActual][i] == 1 and i != padre:
                        return False
        return True
    
    def BEP(self, nodo):
        visitados=[False]*self.__numVertices
        pila=[nodo]
        while pila:
            vertice=pila.pop()
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__numVertices):
                    
                    if self.__matriz[vertice][i]==1 and not visitados[i]:
                        pila.append(i)
        print (visitados)
        return all(visitados)
    
    def BEA(self, nodo):
        visitados=[False]*self.__numVertices
        pila=[nodo]
        while pila:
            vertice=pila.pop(0)
            if not visitados[vertice]:
                visitados[vertice]=True
                for i in range(self.__numVertices):
                    
                    if self.__matriz[vertice][i]==1 and not visitados[i]:
                        pila.append(i)
        print (visitados)

        return all(visitados)#NO ESTA VISITANDO A TODOS LOS VERTICES, ALGO PASA CUANDO UNA FINA ES TODO 0   


if __name__ == "__main__":
    g = Secuencial(5)
    
    g.agregarArista(0,1)
    g.agregarArista(0,2)
    
    
    g.agregarArista(2,1)
    
    g.agregarArista(1,3)
    g.agregarArista(1,4)
    g.agregarArista(2,3)
    g.agregarArista(3,4)
    #g.agregarArista(4,1)
    #g.agregarArista(4,0) #SI LA COLUMNA DEL 0 ES TODO 0, NO RECORRE TODOS LOS VERTUCES
    
    g.mostrar()
    g.adyacentes(2)
    g.gradoSalida(1)
    g.gradoEntrada(3)

    g.nodoFuente(0)
    print(f"NUMERO DE NODOS FUENTES: {g.nodosFuentes()}")
    g.nodoSumidero(3)
    
    g.camino(0, 4)
    
    if g.conexo():
        print("grafo conexo")
    else:
        print("no es conexo")

    if g.aciclico():
        print("grafo aciclico")
    else:
        print("no es aciclico")
    
    g.nodoFuente(1)
    
    a=int(input("Ingrese un vertice para empezar la busqueda en profundidad:"))
    if g.BEP( a)!=False:
        print ("Todos los vertices visitados")
    else:  print ("No todos los vertices fueron visitados")
    
    b=int(input("Ingrese un vertice para empezar la busqueda en amplitud:"))
    if g.BEA( b)!=False:
        print ("Todos los vertices visitados")
    else:  print ("No todos los vertices fueron visitados")