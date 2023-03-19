from NODOS import nodoPila as nP
from NODOS import Pila as P

class TorresDeHanoi(object):

    def __init__(n, origen, destino, auxiliar):
        n.n = n
        n.origen = origen
        n.destino = destino
        n.auxiliar = auxiliar

    def mover(n, origen, destino):
        P.apilar(destino, P.desapilar(origen))

    def resolver(n, origen, destino, auxiliar):
        if n == 1:
            n.mover(origen, destino)
        else:
            n.resolver(origen, auxiliar, destino, n-1)
            n.mover(origen, destino)
            n.resolver(auxiliar, destino, origen, n-1)

    def __str__(n):
        return "Torres de Hanoi de %d discos" % n.n
    
    
if __name__ == "__main__":
    p1 = P()
    p2 = P()
    p3 = P()
    for i in range(5, 0, -1):
        P.apilar(p1, i)
    print ("Pila 1:", p1)
    print ("Pila 2:", p2)
    print ("Pila 3:", p3)
    print
    hanoi = TorresDeHanoi(5, p1, p2, p3)
    hanoi.resolver(p1, p2, p3)
    print ("Pila 1:", p1)
    print ("Pila 2:", p2)
    print ("Pila 3:", p3)