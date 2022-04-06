from time import sleep
from depositorecebe import *
import depositoconferencia

def menu_deposito():
        print('Sistema One v1.0.0')
        print('1 - Recebimento')
        print('2 - Conferência')
        print('3 - Sair do Sistema')
        escolha = int(input('Sua opção: '))

        if escolha == 1:
            recebe_mercadoria()

        elif escolha == 2:
           conferencia_deposito()

        elif escolha == 3:
            sleep(2)
            exit()
