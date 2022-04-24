from time import sleep

import geral
from sistema import linha_2, linha, cabecalho
from users import operations_users, operations_password

def funcionario():
    print(linha_2())
    func = input('Digite o nome: ')
    print(linha())
    sen = input('Digite a senha: ')
    if func not in operations_users:
        operations_users.append(func)
    if sen not in operations_password:
        operations_password.append(sen)
        print("Sucesso no cadastro de {}!".format(func))
        sleep(1)


def listar_funcionarios():
    print(operations_users)
    sleep(1)

def menu_funcionario():
    while True:
        cabecalho('Menu Funcionário')
        print(linha_2())
        print('[1] - Cadastrar Funcionários')
        print('[2] - Listar Funcionarios')
        print('[3] - Menu Gerencial')
        print(linha())
        choice = int(input('Sua opção: '))

        if choice == 1:
            funcionario()

        elif choice == 2:
            listar_funcionarios()

        elif choice == 3:
            geral.menu_gerencial(auth=True)