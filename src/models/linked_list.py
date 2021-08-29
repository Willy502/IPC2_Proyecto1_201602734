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
        counter = 0
        while current != None:
            counter += 1
            print(counter,". ", current.position.gas)
            current = current.next