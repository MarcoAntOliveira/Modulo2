# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista = []
lista_refazer = []
tam = 0
tam1= 0
while(True):
    print("comandos: listar, desfazer, refazer\n")
    acess = input("Digite uma tarefa ou comando: \n")

    if(acess == "listar"):
        if(tam == 0):
            print("Não há o que listar\n")  
            continue  
        print("TAREFAS")
        for i  in lista:
            print(i)
            print("\n")

    elif(acess =="desfazer"):
        if( tam == 0 ):
            print("Não há o que desfazer\n")
            continue
        elemento = lista.pop()
        tam = len(lista)
        lista_refazer.append(elemento)
        tam1 = len(lista_refazer)

    elif(acess == "refazer"):    
        if( tam1 == 0 ):
            print("Nao ha o que refazer\n")
        elemento = lista_refazer.pop()
        tam1 = len(lista_refazer)
        lista.append(elemento)
        tam = len(lista)
    else:
        lista.append(acess) 
        tam = len(lista)

        
    