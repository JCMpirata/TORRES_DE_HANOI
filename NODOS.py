class nodoPila:

    info, sig = None, None

class Pila(object):

    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def apilar(pila, dato):
        nodo = nodoPila()
        nodo.info = dato
        nodo.sig = pila.cima
        pila.cima = nodo
        pila.tamanio += 1

    def desapilar(pila):
        x = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
        return x
    
    def pilaVacia(pila):
        return pila.cima == None
    
    def tamanioPila(pila):
        return pila.tamanio
    
    def encimaPila(pila):
        if pila.cima is not None:
            return pila.cima.info
        else:
            return None
        
    def barridoPila(pila):
        aux = Pila()
        while not pila.pilaVacia():
            dato = pila.desapilar()
            print(dato)
            aux.apilar(aux, dato)

        while not aux.pilaVacia():
            dato = aux.desapilar()
            pila.apilar(pila, dato)

        
    
        