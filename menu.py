from authentication import auth_user


def print_menu_number():

    print('Sistema One v1.0.0')
    print('1 - Conferente Depósito')
    print('2 - Conferente Loja')
    print('3 - Gerenciamento Geral')
    print('4 - Sair do Sistema')
    menu_number = int(input('Sua opção: '))

    if menu_number == 4:
        return [4]

    username = input('Informe seu usuário: ')
    password = input(f'Informe a senha do usuario {username}: ')
    return [menu_number, username, password]


def run_menu(menu_number, username, password):

    auth_user(menu_number, username, password)


def conferente_loja_menu():
    print('Conferente loja menu')


def conferente_gerenciamento_geral_menu():
    print('Gerencialmento geral menu')


def conferente_sair_menu():
    print('Saindo!')
