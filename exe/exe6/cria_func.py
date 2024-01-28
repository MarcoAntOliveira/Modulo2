# Exercício - Adiando execução de funções
def criar_soma(soma):
    def somar(numero):
        return soma + numero
    return somar

def mult(x, y):
    return x * y

def  sum(x , y):
    return x + y

def mod(x, y):
    return x % y

def criar_multiplicador(multiplica):
    def multiplicar(numero):
        return multiplica* numero
    return multiplicar

def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def intern(y):
        return funcao(x , y)
    return intern


#soma_com_cinco = criar_funcao(soma, 5)
#multiplica_por_dez = criar_funcao(multiplica, 10)