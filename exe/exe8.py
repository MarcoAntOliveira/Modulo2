"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:

=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

def soma(lista_a, lista_b):
    int_max = min(len(lista_a),len(lista_b))
    return [
        lista_a[i] + lista_b[i] for i in range(int_max)
    ]

def soma_maior(lista_a, lista_b): 
    int_max= max(len(lista_a), len(lista_b))
    if int_max > len(lista_a):
        for i in range(len(lista_a), int_max):
            lista_a.append(0)
    else:
         for i in range(len(lista_b), int_max):
            lista_b.append(0)        
    return[
        lista_a[i] + lista_b[i] for i in range(int_max)
    ]   

def show_list(listc):
    for i in listc:
        print(i)

lista_c = soma(lista_a, lista_b)
lista_d= soma_maior(lista_a, lista_b)
show_list(lista_c)
show_list(lista_d)