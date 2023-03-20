class SNode:
    def __init__(self, elem, next =None):
        self.elem = elem
        self.next = next


class Pila:
    def __init__(self):
        self._head = None
        self.len = 0

    def push(self, e):
        newNode = SNode(e, self._head)
        self._head = newNode
        self.len += 1

    def pop(self):
        res = None
        if not self.isEmpty():
            res = self._head.elem
            self._head = self._head.next
        else:
            print("Fila vacia!!!")
        return res

    def isEmpty(self):
        return self._head is None

    def __len__(self):
        return self.len

    def __str__(self):

        result = ""
        while not self.isEmpty():
            result += f"{self._head.elem}, "
            self._head = self._head.next
            self.len -= 1
        return result

        
    
        