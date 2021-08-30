import xml.etree.ElementTree as ET
from src.models.linked_list import *
from src.models.ground import *
from src.proyecto_singleton import *
from src.models.position import *
from commons.helper import *

class Xml:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        tree = ET.parse(self.file_path)
        grounds = tree.getroot()

        print("Ingresa el nombre del terreno")
        print("> ", end="")
        ground_name = input()

        found = False

        for terrain in grounds:
            name = terrain.attrib["nombre"]
            ground = Ground(name)
            positions = LinkedList()

            if name == ground_name:
                found = True

                for element in terrain:
                    
                    if element.tag == "posicioninicio":
                        init_dict = {}
                        for pos_in in element:
                            init_dict[pos_in.tag] = int(pos_in.text)
                        ground.pos_init = init_dict

                    elif element.tag == "posicionfin":
                        end_dict = {}
                        for pos_end in element:
                            end_dict[pos_end.tag] = int(pos_end.text)
                        ground.pos_end = end_dict

                    else:
                        pos = Position(x=int(element.attrib["x"]), y=int(element.attrib["y"]), gas=int(element.text))
                        positions.insert(pos)

                ground.positions = positions

                print("")
                positions.build_matrix()
                positions.run(x_start=ground.pos_init["x"], y_start=ground.pos_init["y"], x_finish=ground.pos_end["x"], y_finish=ground.pos_end["y"])
                ProyectoSingleton().positions = positions
                ProyectoSingleton().name = name
                ProyectoSingleton().ground = ground
                print(name, "procesado exitosamente")

        if found != True:
            print("")
            print("Terreno no encontrado")