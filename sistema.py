def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033(31mERRO: por favor, digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31 Usuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

def linha(tam=26):
    return '-' * tam

def linha_2(tam=26):
    return '=' * tam

def cabecalho(txt):
    print(linha_2())
    print(txt.center(5))
    print(linha_2())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiaint('\033[32mSua opção: \033[m')
    return opcao
