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
import os
def listar(lista):
    if not  lista :
            print("Não há o que listar\n")  
            return 
    print("TAREFAS")
    for i  in lista:
        print(f"{i}\n")
        

def desfazer(lista ,  lista_refazer):
    if not lista:
        print("Não há o que desfazer\n")
    
    elemento = lista.pop()
    lista_refazer.append(elemento)
    

def refazer(lista, lista_refazer):
    if not lista_refazer:
        print("Nao ha o que refazer\n")
    elemento = lista_refazer.pop()
    lista.append(elemento)
     

lista = []
lista_refazer = []

while(True):
    print("comandos: listar, desfazer, refazer\n")
    acess = input("Digite uma tarefa ou comando: \n")

    if(acess == "listar"):
        listar(lista)
       
    elif(acess =="desfazer"):
        desfazer(lista, lista_refazer)
        
    elif(acess == "refazer"):    
        refazer(lista, lista_refazer)

    elif acess == "clear":
        os.system("clear")

    else:
        lista.append(acess) 
        tam = len(lista)

        
    