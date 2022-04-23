from time import sleep


def menu_deposito():
    while True:
        cabecalho('        DEPÓSITO')
        usuario_deposito = input('Digite seu usuario: ')
        senha_deposito = int(input('Digite sua senha:   '))

        if usuario_deposito in operations_users:
            if senha_deposito in operations_password:
                print('Bem vindo {}!' .format(usuario_deposito))
                sleep(1)
                print(linha_2())
                print('[1] - Recebimento')
                print('[2] - Conferência')
                print('[3] - Sair do Sistema')
                print(linha())
                escolha = int(input('Sua opção: '))

        if usuario_deposito not in operations_users:
            print('Usuario não permitido!')
            sleep(1)
