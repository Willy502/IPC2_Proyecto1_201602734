import xml.etree.ElementTree as ET
import time
from os import system, name as sys_name
from src.models.linked_list import *
from src.models.ground import *
from src.proyecto_singleton import *

class Xml:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        tree = ET.parse(self.file_path)
        grounds = tree.getroot()

        linked_list = LinkedList()

        for terrain in grounds:
            name = terrain.attrib["nombre"]
            print("Leyendo ", name, " ...")
            time.sleep(2)
            ground = Ground(name)
            first = True

            for element in terrain:
                
                if element.tag == "posicioninicio":
                    print("Leyendo posicion Inicial ...")
                    time.sleep(2)
                    init_dict = {}
                    for pos_in in element:
                        init_dict[pos_in.tag] = pos_in.text
                    ground.pos_init = init_dict

                elif element.tag == "posicionfin":
                    print("Leyendo posicion Final ...")
                    time.sleep(2)
                    end_dict = {}
                    for pos_end in element:
                        end_dict[pos_end.tag] = pos_end.text
                    ground.pos_end = end_dict

                else:
                    if first:
                        print("Leyendo posiciones ...")
                        time.sleep(2)
                        first = False
                        
                    pos_dict = {
                        "x" : element.attrib["x"],
                        "y" : element.attrib["y"],
                        "gas" : element.text
                    }
                    ground.positions.append(pos_dict)

            linked_list.insert(ground)
            print(name, " cargado exitosamente")
            time.sleep(2)

            if sys_name == 'nt':
                _ = system('cls')
        
            else:
                _ = system('clear')

        ProyectoSingleton().linked_list = linked_list
        print("Lista enlazada creada exitósamente")