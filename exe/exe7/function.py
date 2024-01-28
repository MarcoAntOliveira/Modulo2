
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
def ziper(list1 ,  list2):
    is_list(list1)
    is_list(list2)
    set1 = set()
    count1 = 0
    count2 =0
    list3 = [] 
    list4 = []
    set1 = ()
    count1 = min(len(list1), len(list2))
    list3 = []

    while(count2 < count1):
        list4 = []
        yield list4.append(list1[count2])
        yield list4.append(list2[count2])
        set1 = tuple(list4)
        list3.append(set1)
        count2+=1
    return list3
  
        
def is_list(list1):
    if not isinstance(list1, list):
        raise TypeError('param deve ser uma lista')

def insert_list(list1, list4, i):
    list4.append(list1[i])
    return list4


def insert(set1, list3):
    list3.append(tuple(set1))   
    return list3  
 
def show_list(list3):
    for i in list3:
        print(i) 
 