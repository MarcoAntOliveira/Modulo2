# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def dobra(numero):
    numero *=2
    return numero     

'''def triplica(numero):
    numero *=3
    return numero    

def quintuplica(numero):
    numero *=5
    return numero    

def quadruplicar(numero):
    numero *=4
    return numero'''
    
def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar

duplicar = cria_multiplicador(2)
potencia_dez = cria_multiplicador(10**3)
print(duplicar(2))
print(duplicar(4))
print(duplicar(6))
print(potencia_dez(2))
print(potencia_dez(59))


