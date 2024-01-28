carros = {
    0 : ["Chevrolet Tracker" , 120],
    1 : ["Chevrolet Onix"    ,  90],
    2 : ["Chevrolet Spin"    , 150],
    3 : ["Hyundai HB20"      ,  85],
    4 : ["Hyunday Tucson"    , 120],
    5 : ["Fiat Uno"          ,  60],
    6 : ["Fiat Mobi"         ,  70],
    7 : ["Fiat Pulse"        , 130]

}
carros_alugados = [] 

def mostrar_portifólio(carros):
    for chave in carros:
        if chave in carros_alugados:
           continue
        print(f"[{chave}] {carros[chave][0]} - R$ {carros[chave][1]}/ por dia")


def alugar_carros(carros):
    mostrar_portifólio(carros)
    cliente =int(input("escolha o codigo do carro?"))
    dias = int(input("Por quantos dias deseja alugar o carro?"))

    print(f"Você escolheu {carros[cliente][0]} por {dias} dias" )
    alugar =int(input(f"O aluguel totaliza {carros[cliente][1]*dias}, deseja alugar ?\n\n 0- SIM| 1 - NÂO\n"))
    if alugar == 0:
        carros_alugados.append(cliente)
        print(f"Parabéns você alugou {carros[cliente][0]} por {dias} dias\n")
    
def devolver_carros(carros):
    if(len(carros_alugados)):
        print("não carros alugados\n")
    for valor, i in carros_alugados:
        print(valor ,  i)
    devolucao = int(input("carro para devolução\n"))
    carros_alugados.pop(devolucao)

while(True):
    print("===========================\n")
    print("Bem_vindo A locadora de carros\n")
    print("===========================\n")
    options ={
        0 : lambda: mostrar_portifólio(carros),
        1 : lambda: alugar_carros(carros),
        2 : lambda: devolver_carros(carros)
    }

    print("o que deseja fazer?")
    choose  = int(input("0 - Mostrar Portifólio| 1- Alugar um carro | 2- Devolver um carro\n\n"))
    option = options.get(choose)
    option()

