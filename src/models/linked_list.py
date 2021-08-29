from .nodo import *

class LinkedList:

    def __init__(self):
        self.first = None

    def insert(self, position):
        if self.first is None:
            self.first = Nodo(position = position)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = Nodo(position = position)

    def run(self):
        current = self.first
        while current != None:
            print(current.position.x, current.position.y, current.position.gas)
            current = current.next

    def search(self, x, y):
        current = self.first
        while current != None:
            if current.position.x == x and current.position.y == y:
                return current
            current = current.next
        return None

    def build_matrix(self):
        current = self.first
        while current != None:

            # Left node
            left = self.search(x=current.position.x-1, y=current.position.y)
            if left != None:
                current.position.left = left

            # right node
            right = self.search(x=current.position.x+1, y=current.position.y)
            if right != None:
                current.position.right = right

            # top node
            top = self.search(x=current.position.x, y=current.position.y-1)
            if top != None:
                current.position.top = top

            # bottom node
            bottom = self.search(x=current.position.x, y=current.position.y+1)
            if bottom != None:
                current.position.bottom = bottom

            current = current.next