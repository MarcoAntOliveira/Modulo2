# copy, sorted, produtos.sort
import pprint
import copy
def p(v):
    pprint.pprint(v, sort_dicts= False, width=10)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
novos_produtos =[
        {**produto, 'preco': produto['preco'] * 1.10}
        for produto in copy.deepcopy(produtos)
    ] 

p(produtos)
p(novos_produtos)
# Gere novos_produtos por deep copy (cópia profunda)
# Ordene os produtos por nome decrescente (do maior para menor)
produtos_ordenados_nome = sorted(
    copy.deepcopy(produtos), 
    key=lambda item: item['nome'], reverse=True
    ) 

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),   
    key=lambda item: item['preco']
    )

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

