from cria_func import criar_soma, criar_multiplicador, sum, mult, criar_funcao, mod

soma_dois = criar_soma(2)
multiplica_por_dez = criar_multiplicador(10)
soma_cinco = criar_funcao(sum , 5)
multiplica_por_7 = criar_funcao(mult, 7)
mod_3 = criar_funcao(mod, 3)
print(multiplica_por_7(7))
print(soma_cinco(75))
print(soma_dois(5))
print(multiplica_por_dez(97))
print(mod_3(97))