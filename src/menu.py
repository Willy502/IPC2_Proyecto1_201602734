from .options import *
from .proyecto_singleton import *
from commons.graph import *
from commons.gen_xml import *

class Menu:

    def __init__(self):
        self.create_menu()

    def create_menu(self):
        print("Menú principal:")
        print("1. Cargar archivo")
        print("2. Procesar archivo")
        print("3. Escribir archivo salida")
        print("4. Mostrar datos del estudiante")
        print("5. Generar gráfica")
        print("6. Salir")
        print("> ", end="")
        answer = input()
        print("------------------------------------\n")
        self.select_menu_option(answer)

    def select_menu_option(self, option):

        if option == "1":
            Options().load_file()

        elif option == "2":
            if ProyectoSingleton().file is None:
                print("Para utilizar esta opción debes cargar una ruta primero")
            else:
                Options().process_xml()

        elif option == "3":
            if ProyectoSingleton().file is None:
                print("Para utilizar esta opción debes cargar una ruta primero")
            else:
                GenXml().generate(ProyectoSingleton().ground, ProyectoSingleton().finish)

        elif option == "4":
            Options().student_information()

        elif option == "5":
            if ProyectoSingleton().file is None:
                print("Para utilizar esta opción debes cargar una ruta primero")
            else:
                Graph().build_graph(positions=ProyectoSingleton().positions, name=ProyectoSingleton().name)

        elif option == "6":
            quit()
        else:
            print("Selecciona una opción válida")

        print("")
        self.create_menu()