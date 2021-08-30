import xml.etree.cElementTree as ET
from xml.dom import minidom
from commons.helper import *

class GenXml:

    def generate(self, ground, finish):
        Helper().clear_screen(wait=False)
        print("Generando XML...")
        Helper().clear_screen(wait=True)

        terreno = ET.Element('terreno')
        terreno.set('nombre', ground.name)
        pos_inicio = ET.SubElement(terreno, 'posicioninicio')
        init_x = ET.SubElement(pos_inicio, 'x')
        init_x.text = str(ground.pos_init["x"])
        init_y = ET.SubElement(pos_inicio, 'y')
        init_y.text = str(ground.pos_init["y"])

        pos_fin = ET.SubElement(terreno, 'posicionfin')
        fin_x = ET.SubElement(pos_fin, 'x')
        fin_x.text = str(ground.pos_end["x"])
        fin_y = ET.SubElement(pos_fin, 'y')
        fin_y.text = str(ground.pos_end["y"])

        current = ground.positions.first
        suma = 0
        while current != None:
            if current.position.route == True:
                suma += current.position.gas

            current = current.next

        combustible = ET.SubElement(terreno, 'combustible')
        combustible.text = str(suma)
        current = finish
        route_list = []
        while current != None:
            route_list.append(current)
            current = current.comming_from

        for element in reversed(route_list):
            pos = ET.SubElement(terreno, 'posicion')
            pos.set('x', str(element.x))
            pos.set('y', str(element.y))
            pos.text = str(element.gas)
        
        data = minidom.parseString(ET.tostring(terreno))
        file = open("output/terreno.xml", "w")
        new_data = data.toprettyxml()
        file.write(new_data)

        print("XML generado exitosamente")
        Helper().clear_screen(wait=True)
        