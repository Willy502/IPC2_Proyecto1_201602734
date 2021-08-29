import time
from os import system, name as sys_name

class Helper:

    def clear_screen(self, wait):
        if wait:
            time.sleep(2)
        if sys_name == 'nt':
            _ = system('cls')
            
        else:
            _ = system('clear')