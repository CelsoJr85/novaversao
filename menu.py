""" MENU PRINCIPAL """
from sistema import *
from deposito import menu_deposito
from geral import menu_gerencial

cabecalho(' BEM VINDO AO SISTEMA ONE')

while True:
    print('[1] - Conferente Depósito')
    print('[2] - Conferente Loja')
    print('[3] - Gerência')
    print('[4] - Sair do Sistema')
    print(linha())
    menu_number = int(input('Sua opção: '))

    if menu_number == 1:
        menu_deposito()

    if menu_number == 2:
        loja.py()

    if menu_number == 3:
        menu_gerencial()

    if menu_number == 4:
        sleep(1)
        break
