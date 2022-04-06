from time import sleep
from geralce import *
from geralrelatorio import *
from geralre import *

def menu_geral():
    while True:
        print('Sistema One v1.0.0')
        print('1 - Cadastro de Entrada')
        print('2 - Relatório de Produtos Cadastrados')
        print('3 - Relatorio Entrada')
        print('4 - Sair do Sistema')

        opcao = int(input('Sua opção: '))
        if opcao == 1:
            cadastro_produto()

        if opcao == 2:
            relatorio()

        if opcao == 3:
            relatorio_deposito()

        if opcao == 4:
            sleep(2)
            exit()
