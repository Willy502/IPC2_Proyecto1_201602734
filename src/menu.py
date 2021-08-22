from .options import *

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
            print(option)

        elif option == "2":
            print(option)

        elif option == "3":
            print(option)

        elif option == "4":
            Options().student_information()

        elif option == "5":
            print(option)

        elif option == "6":
            quit()
        else:
            print("Selecciona una opción válida")

        print("")
        self.create_menu()