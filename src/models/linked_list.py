from .nodo import *
import random
from commons.helper import *

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

    def search(self, x, y):
        current = self.first
        while current != None:
            if current.position.x == x and current.position.y == y:
                return current.position
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

    def random(self, pos_1, pos_2):
        ran = random.randint(1, 10)
        if ran%2 != 0:
            return pos_1
        else:
            return pos_2

    def calculate_minimum(self, position, previous):
        # Left node
        left = self.search(x=position.x-1, y=position.y)
        if left in previous:
            left = None
        # right node
        right = self.search(x=position.x+1, y=position.y)
        if right in previous:
            right = None
        # top node
        top = self.search(x=position.x, y=position.y-1)
        if top in previous:
            top = None
        # bottom node
        bottom = self.search(x=position.x, y=position.y+1)
        if bottom in previous:
            bottom = None

        horizontal = None
        vertical = None

        if left is None:
            horizontal = right
        elif right is None:
            horizontal = left
        elif left.gas > right.gas:
            horizontal = right
        elif left.gas < right.gas:
            horizontal = left
        elif left.gas == right.gas:
            horizontal = self.random(left, right)

        if top is None:
            vertical = bottom
        elif bottom is None:
            vertical = top
        elif top.gas > bottom.gas:
            vertical = bottom
        elif top.gas < bottom.gas:
            vertical = bottom
        elif top.gas == bottom.gas:
            vertical = self.random(top, bottom)

        if horizontal is None:
            return vertical
        elif vertical is None:
            return horizontal
        elif horizontal.gas > vertical.gas:
            return vertical
        elif horizontal.gas < vertical.gas:
            return horizontal
        elif horizontal.gas == vertical.gas:
            return self.random(horizontal, vertical)

    def run(self, x_start, y_start, x_finish, y_finish):

        Helper().clear_screen(wait=False)
        start = self.search(x=x_start, y=y_start)
        finish = self.search(x=x_finish, y=y_finish)
        previous = []
        current = start

        print("Buscando la mejor ruta...")
        Helper().clear_screen(wait=True)
        while current != finish:
            print("X:", current.x, "Y:", current.y, "GAS:", current.gas)
            previous.append(current)
            current = self.calculate_minimum(position=current, previous=previous)

        total_gas = 0
        for data in previous:
            print(data.x, data.y, data.gas)
            total_gas += data.gas
        
        print("Calculando combustible...")
        Helper().clear_screen(wait=True)
        print("Combustible gastado", total_gas)