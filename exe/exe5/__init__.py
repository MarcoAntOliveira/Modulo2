from mod_produto import produtos
from fuctions import p, c

print('produtos\n')
p(produtos)
novos_produtos =[
        {**produto, 'preco': produto['preco'] * 1.10}
        for produto in c(produtos)
    ]
print('novos produtos\n')
p(novos_produtos)

produtos_ordenados_nome = sorted(
    c(produtos), 
    key=lambda item: item['nome'], reverse=True
) 
print('produtos ordenados por nome\n')
p(produtos_ordenados_nome)

produtos_ordenados_por_preco = sorted(
    c(produtos),   
    key=lambda item: item['preco']
    )
print('novos produtos ordenados por preco\n')
p(produtos_ordenados_por_preco)