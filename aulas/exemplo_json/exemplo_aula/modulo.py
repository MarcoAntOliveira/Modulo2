import json
import os

lista = []
lista.append("marcos")
lista.append("maria")



BASE_DIR =  os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-python1.json')

with open(SAVE_TO, 'w') as file:
    json.dump(lista, file, indent = 2) #pega os dados dentro do codigo
    print (json.dumps(lista, indent = 2))

# carregando aqruivo de fora 
BASE_DIR = os.path.dirname(__file__)
JSON_FILE =  os.path.join(BASE_DIR, 'arquivo-python1.json') 

with open(JSON_FILE, 'r') as file:
    pessoas= json.load(file)# carreaga dados externos ao codigo
    print(json.dumps(lista))

    #for pessoa in pessoas:
     #   print(pessoa["nome"])
"""
json_string = '''
[{"nome": "maria", "sobrenome": " viera"}, {"nome": "marcos", "sobrenome": "antonio"}] 
'''
pessoas = json.loads(json_string)
for pessoa in pessoas:
    print(pessoa["nome"])
"""    