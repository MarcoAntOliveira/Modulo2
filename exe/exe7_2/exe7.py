# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def ziper(list1, list2):
    inter_max= min(len(list1), len(list2))

    return[
        (list1[i], list2[i]) for i in range(inter_max)
    ]


print(ziper(list1, list2))