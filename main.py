from time import sleep
from menu import *
from deposito import *
from geral import *

if __name__ == "__main__":

    while True:

        menu_number = print_menu_number()

        if menu_number[0] == 1:

            run_menu(menu_number[0], menu_number[1], menu_number[2])
            menu_deposito()

        elif menu_number[0] == 2:

            run_menu(menu_number[0], menu_number[1], menu_number[2])

        elif menu_number[0] == 3:

            run_menu(menu_number[0], menu_number[1], menu_number[2])
            menu_geral()

        elif menu_number[0] == 4:

            print('Saindo!')
            sleep(2)
            exit()
