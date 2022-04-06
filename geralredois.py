
def arquivo_continuacao():
    arquivo = open('Empresa-001.txt', 'r')
    arquivo.writelines(input('produto: '))
    arquivo.close()
