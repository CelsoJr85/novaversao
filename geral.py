from time import sleep
from sistema import *
from authentication import *

def menu_gerencial():
    while True:
        cabecalho('GERÊNCIA')
        usuario_gerencia = input('Digite seu usuario: ')
        senha_gerencia = int(input('Digite sua senha:   '))

        if usuario_gerencia in management_users:
            if senha_gerencia in management_password:
                print('Bem vindo {}!' .format(usuario_gerencia))
                sleep(1)
                print(linha_2())
                print('[1] - Cadastrar Funcionários')
                print('[2] - Cadastrar Produtos')
                print('[3] - Relatorio')
                print('[4] - Sair do Sistema')
                print(linha())
                escol = int(input('Sua opção: '))

                if escol == 1:
                   funcionario()

                if escol == 2:
                    pass

                if escol == 3:
                    pass

                if escol == 4:
                    sleep(1)
                    break


        if usuario_gerencia not in management_users:
            print('Usuario não permitido!')
            print('Tente novamente!')
            sleep(1)