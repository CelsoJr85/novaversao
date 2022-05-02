"""Cadastro de Administrador e Funcionário"""
import xlsxwriter
from time import sleep

def cadastro_master():
    #Cadastro de Administrador
    new1 = input('Usuário: ')
    new2 = input('Usuário: ')
    new3 = input('Usuário: ')
    new4 = input('Usuário: ')
    senha1 = int(input('Senha: '))
    senha2 = int(input('Senha: '))
    senha3 = int(input('Senha: '))
    senha4 = int(input('Senha: '))

    workbook = xlsxwriter.Workbook('login_sistema.xlsx')
    worksheet = workbook.add_worksheet("1")
    scores = (
        [new1, senha1],
        [new2, senha2],
        [new3, senha3],
        [new4, senha4],
    )
    row = 0
    col = 0
    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1

    workbook.close()
    print('Cadastro de Administrador efetuado com sucesso!')
    sleep(1)
    return True

def cadastro_secundario():
    #Cadastro de funcionarios
    new1 = input('Usuário: ')
    new2 = input('Usuário: ')
    new3 = input('Usuário: ')
    new4 = input('Usuário: ')
    senha1 = int(input('Senha: '))
    senha2 = int(input('Senha: '))
    senha3 = int(input('Senha: '))
    senha4 = int(input('Senha: '))

    workbook = xlsxwriter.Workbook('login_funcionário.xlsx')
    worksheet = workbook.add_worksheet("2")
    scores = (
        [new1, senha1],
        [new2, senha2],
        [new3, senha3],
        [new4, senha4],
    )
    row = 0
    col = 0
    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1

    workbook.close()
    print('Cadastro de funcionário efetuado com sucesso!')
    sleep(1)
    return True
