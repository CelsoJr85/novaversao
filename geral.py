from time import sleep
import authentication as auth_func
from sistema import cabecalho, linha_2, linha
from users import *


def menu_gerencial(auth=False):
    while True:
        if auth is False:
            cabecalho('GERÊNCIA')
            usuario_gerencia = input('Digite seu usuario: ')
            senha_gerencia = int(input('Digite sua senha:   '))
            if usuario_gerencia in management_users:
                if senha_gerencia in management_password:
                    print('Bem vindo {}!'.format(usuario_gerencia))
                    sleep(1)
                    print(linha_2())
                    print('[1] - Cadastrar Funcionários')
                    print('[2] - Cadastrar Produtos')
                    print('[3] - Relatorio')
                    print('[4] - Sair do Sistema')
                    print(linha())
                    escol = int(input('Sua opção: '))

                    if escol == 1:
                        auth = auth_func.funcionario()

                    if escol == 2:
                        pass

                    if escol == 3:
                        pass

                    if escol == 4:
                        sleep(1)
                        break

                else:
                    print('Senha não reconhecida, tente novamente.')
                    sleep(1)
            else:
                print('Usuario não permitido!')
                print('Tente novamente!')
                sleep(1)

        elif auth is True:
            print(linha_2())
            print('[1] - Cadastrar Funcionários')
            print('[2] - Cadastrar Produtos')
            print('[3] - Relatorio')
            print('[4] - Sair do Sistema')
            print(linha())
            escol = int(input('Sua opção: '))

            if escol == 1:
                auth = auth_func.funcionario()

            if escol == 2:
                pass

            if escol == 3:
                pass

            if escol == 4:
                sleep(1)
                break
