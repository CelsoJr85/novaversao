operations_users = {'Rafael': '1234', 'José': '1234', 'Maria': '1234', 'Antônio': '1234', 'César': '1234'}
management_users = {'Celso': '1234', 'Fernanda': '4321'}

"""
    Importante:
        Apenas usuários do grupo management users tem permissão de acessar o modulo gerenciamento geral.
    
    O menu 1 e 2 são permitidos para todos os usuários autenticados
    O menu 3 apenas para usuários da lista management_users
"""


def auth_user(menu_number, username, password):

    if (menu_number == 1 or menu_number == 2) and (
            (username in operations_users and operations_users[username] == password)
            or
            (username in management_users.keys() and management_users[username] == password)
    ):

        print(f"Ola {username} bem vindo!")
        return 1

    elif menu_number == 3 and (
            username in management_users.keys() and management_users[username] == password
    ):

        print(f"Ola {username} bem vindo você é do grupo management users!")
        return 1

    else:

        print(f'Ooops {username}, não consegui te dar acesso! Verifique suas permissões e/ou usuário e senha :(')
        return 0
