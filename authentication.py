from time import sleep
from sistema import *

operations_users = ['celso', 'fernanda', 'rafael', 'josé', 'maria', 'antônio', 'cesar']
operations_password = [2022]
management_users = ['celso', 'fernanda']
management_password = [1985]

def funcionario():
    print(linha_2())
    func = input('Digite o nome: ')
    print(linha())
    sen = input('Digite a senha: ')
    if func not in operations_users:
        operations_users.append(func)
    if sen not in operations_password:
        operations_password.append(sen)
        print("Sucesso no cadastro de {}!" .format(func))
        sleep(1)
        exit()
