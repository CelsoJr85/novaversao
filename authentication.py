from time import sleep
from sistema import linha_2, linha
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
        return True
