from time import sleep



def recebe_mercadoria():
    while True:
        recebimento = []
        quantidade = []
        datavalidade = []
        recebe = input('produto: ')
        if recebe not in recebimento:
            recebimento.append(recebe)
            qtde = input('Quantidade: ')
            if qtde not in quantidade:
                quantidade.append(qtde)
                validade = input('Validade:')
                if validade not in datavalidade:
                    datavalidade.append(validade)
                    print('Produto Adicionado!')
                    sleep(2)
        else:
            print('Produto não pertence ao lote!')