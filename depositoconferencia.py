import json

def conferencia_deposito():
    with open('depositoarquivo.json', 'r') as fp:
        meu_dicionario = json.load(fp)
    print(meu_dicionario)
