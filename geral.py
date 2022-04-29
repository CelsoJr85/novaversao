from time import sleep
from sistema import cabecalho, linha_2, linha
from users import *
from authentication import menu_funcionario
import pandas as pd

def menu_gerencial():
    while True:
        tabela_usuario = pd.read_excel("login_sistema.xlsx", sheet_name="1", usecols="A:D")
        usuario = input('Usuário: ')
        if usuario in tabela_usuario:
            tabela_senha = pd.read_excel('login_sistema.xlsx', sheet_name="1", usecols="E")
            senhas = input('Senha:')
            for senhas in tabela_senha:
                print(f'Seja bem vindo {usuario}!')
                sleep(1)
                cabecalho('GERENCIAMENTO')
                print('[1] - Funcionários')
                print('[2] - Cadastrar Produtos')
                print('[3] - Relatorio')
                print('[4] - Sair do Sistema')
                print(linha())
                escolha = int(input('Sua opção: '))

                if escolha == 1:
                    menu_funcionario()
                if escolha == 2:
                    pass
                if escolha == 3:
                    pass
                if escolha == 4:
                    sleep(1)
                    break

            else:
                print('Senha errada! Tente novamente.')
                sleep(1)
        else:
            print('Usuario não reconhecido, tente novamente.')
            sleep(1)