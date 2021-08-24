from .proyecto_singleton import *
from .xml import *

class Options:

    def student_information(self):
        print("Wilfred Alejandro Barrios Ola")
        print("201602734")
        print("Introducción a la Programación y computación 2 sección 'A'")
        print("Ingeniería en ciencias y sistemas")
        print("4to Semestre")

    def load_file(self):
        print("Ingrese la ruta del archivo")
        print(" > ", end="")
        answer = input()
        ProyectoSingleton().file = answer
        print("Ruta almacenada exitosamente")

    def process_xml(self):
        xml = Xml(ProyectoSingleton().file)
        xml.read()
    