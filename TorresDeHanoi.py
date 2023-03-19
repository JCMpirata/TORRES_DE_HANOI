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
    num_discos = input("Ingrese el numero de discos: ")
    torres = TorresDeHanoi(num_discos, P(), P(), P())
    for i in range(num_discos, 0, -1):
        P.apilar(torres.origen, i)
        