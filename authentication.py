from time import sleep
import geral
from sistema import linha_2, linha, cabecalho
from cadastrogeral import cadastro_master, cadastro_secundario

def menu_funcionario():
    while True:
        cabecalho('Menu Funcionário')
        print(linha_2())
        print('[1] - Cadastrar Administrador')
        print('[2] - Cadastrar Funcionarios')
        print('[3] - Listar Todos')
        print('[4] - Menu Gerencial')
        print(linha())
        choice = int(input('Sua opção: '))

        if choice == 1:
            cadastro_master()

        elif choice == 2:
            cadastro_secundario()

        elif choice == 3:
            pass

        elif choice == 4:
            return True
