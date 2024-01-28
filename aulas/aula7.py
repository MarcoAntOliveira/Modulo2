try:
    a= 16
    b= 0
    print('linha1'[1000])
    c = a/b
    print('linha2')
except  ZeroDivisionError:
    print("dividiu por zero")
except  NameError:
    print('b nao esta definido')
except  (TypeError, IndexError) as error:
    print('typeError + IndexError')
    print('Msg :' , error)
    print('Nome:' , error)
except  Exception:
    print('erro desconhecido')


print('CONTINUAR')