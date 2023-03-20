from NODOS import nodoPila as nP
from NODOS import Pila

class TorresDeHanoi(object):

    def __init__(discos, origen, destino, auxiliar):
        discos.n = discos
        discos.origen = origen
        discos.destino = destino
        discos.auxiliar = auxiliar

    def mover(discos, origen, destino):
        Pila.apilar(destino, Pila.desapilar(origen))

    def resolver(discos, origen, destino, auxiliar):
        if discos == 1:
            discos.mover(origen, destino)
        else:
            discos.resolver(origen, auxiliar, destino, discos-1)
            discos.mover(origen, destino)
            discos.resolver(auxiliar, destino, origen, discos-1)

    def __str__(discos):
        return "Torres de Hanoi con {} discos resuelto en {} movimientos".format(discos.n, 2**discos.n-1)
    
    
if __name__ == "__main__":
    num_discos = input("Ingrese el numero de discos: ")
    torre_origen = Pila()
    torre_auxiliar = Pila()
    torre_destino = Pila()
    torres = TorresDeHanoi(num_discos, torre_origen, torre_auxiliar, torre_destino)
    for i in range(num_discos, 0, -1):
        Pila.apilar(torres.origen, i)
        