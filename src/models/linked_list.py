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

    def find_way(self, start, finish):
        current = start
        current.solved = True
        last = []
        last.append(current)

        while current != finish:
            if len(last) > 1:

                for cur in last:
                    second_last = []
                    horizontal = []
                    vertical = []

                    if cur.left is None or cur.left.solved == True:
                        if cur.right != None and cur.right.solved != True:
                            horizontal.append(cur.right)
                    elif cur.right is None or cur.right.solved == True:
                        if cur.left != None and cur.left.solved != True:
                            horizontal.append(cur.left)
                    elif cur.right.gas > cur.left.gas:
                        if cur.left.solved != True:
                            horizontal.append(cur.left)
                    elif cur.left.gas > cur.right.gas:
                        if cur.right.solved != True:
                            horizontal.append(cur.right)
                    elif cur.left.gas == cur.right.gas:
                        if cur.right.solved != True:
                            horizontal.append(cur.right)
                        if cur.left.solved != True:
                            horizontal.append(cur.left)

                    if cur.top is None or cur.top.solved == True:
                        if cur.bottom != None and cur.bottom.solved != True:
                            vertical.append(cur.bottom)
                    elif cur.bottom is None or cur.bottom.solved == True:
                        if cur.top != None and cur.top.solved != True:
                            vertical.append(cur.top)
                    elif cur.top.gas > cur.bottom.gas:
                        if cur.bottom.solved != True:
                            vertical.append(cur.bottom)
                    elif cur.bottom.gas > cur.top.gas:
                        if cur.top.solved != True:
                            vertical.append(cur.top)
                    elif cur.top.gas == cur.bottom.gas:
                        if cur.bottom.solved != True:
                            vertical.append(cur.bottom)
                        if cur.top.solved != True:
                            vertical.append(cur.top)

                    if len(vertical) > 0 and len(horizontal) > 0:
                        if vertical[0].gas > horizontal[0].gas:
                            for pos in horizontal:
                                second_last.append(pos)
                        elif vertical[0].gas < horizontal[0].gas:
                            for pos in vertical:
                                second_last.append(pos)
                        elif vertical[0].gas == horizontal[0].gas:
                            for pos in horizontal:
                                second_last.append(pos)
                            for pos in vertical:
                                second_last.append(pos)

                    elif len(vertical) > 0 and len(horizontal) == 0:
                        for pos in vertical:
                            second_last.append(pos)

                    elif len(horizontal) > 0 and len(vertical) == 0:
                        for pos in horizontal:
                            second_last.append(pos)

                    for pos in second_last:
                        pos.comming_from = cur
                        pos.solved = True
                        last.append(pos)

                    last.pop(0)
                    fin = False
                    for pos in last:
                        if pos == finish:
                            current = pos
                            fin = True

                    if fin == True:
                        break


            else:
                current = last[0]
                second_last = []
                horizontal = []
                vertical = []

                if current.left is None or current.left.solved == True:
                    if current.right.solved != True:
                        horizontal.append(current.right)
                elif current.right is None or current.right.solved == True:
                    if current.left.solved != True:
                        horizontal.append(current.left)
                elif current.right.gas > current.left.gas:
                    if current.left.solved != True:
                        horizontal.append(current.left)
                elif current.left.gas > current.right.gas:
                    if current.right.solved != True:
                        horizontal.append(current.right)
                elif current.left.gas == current.right.gas:
                    if current.right.solved != True:
                        horizontal.append(current.right)
                    if current.left.solved != True:
                        horizontal.append(current.left)

                if current.top is None or current.top.solved == True:
                    if current.bottom.solved != True:
                        vertical.append(current.bottom)
                elif current.bottom is None or current.bottom.solved == True:
                    if current.top.solved != True:
                        vertical.append(current.top)
                elif current.top.gas > current.bottom.gas:
                    if current.bottom.solved != True:
                        vertical.append(current.bottom)
                elif current.bottom.gas > current.top.gas:
                    if current.top.solved != True:
                        vertical.append(current.top)
                elif current.top.gas == current.bottom.gas:
                    if current.bottom.solved != True:
                        vertical.append(current.bottom)
                    if current.top.solved != True:
                        vertical.append(current.top)

                if len(vertical) > 0 and len(horizontal) > 0:
                    if vertical[0].gas > horizontal[0].gas:
                        for pos in horizontal:
                            second_last.append(pos)
                    elif vertical[0].gas < horizontal[0].gas:
                        for pos in vertical:
                            second_last.append(pos)
                    elif vertical[0].gas == horizontal[0].gas:
                        for pos in horizontal:
                            second_last.append(pos)
                        for pos in vertical:
                            second_last.append(pos)

                elif len(vertical) > 0 and len(horizontal) == 0:
                    for pos in vertical:
                        second_last.append(pos)

                elif len(horizontal) > 0 and len(vertical) == 0:
                    for pos in horizontal:
                        second_last.append(pos)

                last = second_last

                for pos in last:
                    pos.comming_from = current

                if len(last) == 1:
                    last[0].solved = True
                    current = last[0]
                else:
                    for c in last:
                        c.solved = True

    def run(self, x_start, y_start, x_finish, y_finish):

        Helper().clear_screen(wait=False)
        start = self.search(x=x_start, y=y_start)
        finish = self.search(x=x_finish, y=y_finish)

        print("Buscando la mejor ruta...")
        Helper().clear_screen(wait=True)
        self.find_way(start=start, finish=finish)

        total_gas = 0
        current = finish
        while current != None:
            total_gas += current.gas
            current = current.comming_from
        print("Calculando combustible...")
        Helper().clear_screen(wait=True)
        print("Combustible gastado", total_gas)

    def print_route(self):
        print("|")