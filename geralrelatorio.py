import json

def relatorio():
    with open('geralarquivo.json', 'r') as fp:
        my_dict = json.load(fp)
    print(my_dict)
