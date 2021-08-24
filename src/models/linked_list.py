from .nodo import *

class LinkedList:

    def __init__(self):
        self.first = None

    def insert(self, ground):
        if self.first is None:
            self.first = Nodo(ground = ground)
            return
        current = self.first
        while current.next:
            current = current.next
        current.next = Nodo(ground = ground)

    def run(self):
        current = self.first
        while current != None:
            print("Ground: ", current.ground.name)
            current = current.next