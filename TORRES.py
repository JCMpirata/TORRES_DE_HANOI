from NODOS import SNode
from NODOS import Pila


class Nodo:
    def __init__(self, torres, movimientos, padre):
        self.torres = torres
        self.movimientos = movimientos
        self.padre = padre

class Hanoi:
    def __init__(self, n):
        self.n = n
        self.torres = [[], [], []]
        self.torres[0] = list(range(n, 0, -1))
        self.movimientos = 0
        self.solucion = None

    def mover_disco(self, torre_origen, torre_destino):
        if len(self.torres[torre_origen]) == 0:
            print("La torre de origen está vacía")
        elif len(self.torres[torre_destino]) == 0 or \
             self.torres[torre_origen][-1] < self.torres[torre_destino][-1]:
            self.torres[torre_destino].append(self.torres[torre_origen].pop())
            self.movimientos += 1
            print("Movimiento #", self.movimientos)
            print(self.torres)
        else:
            print("Movimiento no permitido")

    def resolver(self):
        raiz = Nodo(self.torres, 0, None)
        nodos = [raiz]
        while nodos and not self.solucion:
            actual = nodos.pop()
            if len(actual.torres[2]) == self.n:
                self.solucion = actual
            else:
                for i in range(3):
                    for j in range(3):
                        if i != j:
                            nueva_torres = [list(t) for t in actual.torres]
                            if nueva_torres[i]:
                                disco = nueva_torres[i][-1]
                                nueva_torres[i].pop()
                                nueva_torres[j].append(disco)
                                movimientos = actual.movimientos + 1
                                nuevo_nodo = Nodo(nueva_torres, movimientos, actual)
                                nodos.append(nuevo_nodo)

        if self.solucion:
            camino = []
            while self.solucion:
                camino.append(self.solucion.torres)
                self.solucion = self.solucion.padre

            camino.reverse()
            for i, t in enumerate(camino):
                print("Movimiento #", i + 1)
                print(t)

if __name__ == "__main__":
    hanoi = Hanoi(3)
    print(hanoi.torres)
    hanoi.resolver()
