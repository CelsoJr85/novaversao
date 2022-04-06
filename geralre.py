import json

def relatorio_deposito():
    with open('depositoarquivo.json', 'r') as fp:
        my_dict = json.load(fp)
    print(my_dict)