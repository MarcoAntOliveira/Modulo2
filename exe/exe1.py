def mult(*args):
    alg = 1
    for numeros in args:
        alg*=numeros

    return alg

def par_impar(num):
    mod = num%2 == 0
    if mod == True:
        return f"o {num} é par"
    
    return f"o {num} é impar"

    #return 'par' if num%2==0 else 'impar'


result = mult(1, 2, 3, 4)
print(result) 
print(par_impar(7))
print(par_impar(546898))
print(par_impar(123457))