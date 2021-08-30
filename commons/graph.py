from graphviz import Digraph
from commons.helper import *

class Graph:

    def build_graph(self, positions, name):
        Helper().clear_screen(wait=False)
        print("Generando grafo...")
        Helper().clear_screen(wait=True)
        dot = Digraph(comment=name, graph_attr={'splines':'polyline', 'rotate':'45'})
        current = positions.first
        while current != None:
            dot.node(current.position.id, str(current.position.gas), shape='circle')
            current = current.next

        current = positions.first
        positions_dict = []
        while current != None:

            existo = False
            
            if current.position.left != None:

                for pos in positions_dict:
                    if (pos["from"] == current.position.id and pos["to"] == current.position.left.id) or (pos["from"] == current.position.left.id and pos["to"] == current.position.id):
                        existo = True
                if existo != True:
                    positions_dict.append(
                        {
                            "from" : current.position.id,
                            "to" : current.position.left.id
                        }
                    )

            existo = False

            if current.position.right != None:
                for pos in positions_dict:
                    if (pos["from"] == current.position.id and pos["to"] == current.position.right.id) or (pos["from"] == current.position.right.id and pos["to"] == current.position.id):
                        existo = True
                if existo != True:
                    positions_dict.append(
                        {
                            "from" : current.position.id,
                            "to" : current.position.right.id
                        }
                    )

            existo = False

            if current.position.top != None:
                for pos in positions_dict:
                    if (pos["from"] == current.position.id and pos["to"] == current.position.top.id) or (pos["from"] == current.position.top.id and pos["to"] == current.position.id):
                        existo = True
                if existo != True:
                    positions_dict.append(
                        {
                            "from" : current.position.id,
                            "to" : current.position.top.id
                        }
                    )

            existo = False

            if current.position.bottom != None:
                for pos in positions_dict:
                    if (pos["from"] == current.position.id and pos["to"] == current.position.bottom.id) or (pos["from"] == current.position.bottom.id and pos["to"] == current.position.id):
                        existo = True
                if existo != True:
                    positions_dict.append(
                        {
                            "from" : current.position.id,
                            "to" : current.position.bottom.id
                        }
                    )

            current = current.next
        
        for pos in positions_dict:
            dot.edge(pos["from"], pos["to"])
        

        dot.render('output/' + name + '.gv', view=True)
        file_name = dot.filepath + ".pdf"
        print("Grafo generado exitosamente")
        Helper().clear_screen(wait=True)