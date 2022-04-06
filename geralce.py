
x1 = input('Empresa: ')
x2 = input()
x3 = input()

arquivo = open('Empresa-001.txt', 'w')
arquivo.write(x1)

with open("Empresa-001.txt", "a+") as arquivo:
    arquivo.append(x2)
    arquivo.close()
