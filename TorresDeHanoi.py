from NODOS import SNode
from NODOS import Pila

class TorresDeHanoi:
    def __init__(self, n):
        self.n = n
        self.torres = [Pila() for i in range(3)]
        self.torres[0].push(n)
        for i in range(n-1, 0, -1):
            self.torres[0].push(i)
    
    def __str__(self):
        result = ""
        for i in range(3):
            result += f"Torre {i}: {self.torres[i]}"
        return result
        
    
    def mover(self, origen, destino):
        if not self.torres[origen].isEmpty():
            if self.torres[destino].isEmpty() or self.torres[origen].peek() < self.torres[destino].peek():
                self.torres[destino].push(self.torres[origen].pop())
                return True
        return False
    
    def resolver(self, n, origen, destino, auxiliar):
        if n > 0:
            self.resolver(n-1, origen, auxiliar, destino)
            self.mover(origen, destino)
            self.resolver(n-1, auxiliar, destino, origen)
        return self.torres[destino]
    
    
if __name__ == "__main__":
    num_discos = int(input("Ingrese el numero de discos: "))
    torres = TorresDeHanoi(num_discos)
    print(torres)
    torres_resolver = torres.resolver(3, 0, 2, 1)
    print(torres_resolver)
        