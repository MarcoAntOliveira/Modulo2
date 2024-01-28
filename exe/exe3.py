# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

count = 97
caractere = ' '
count_acertos = 0
for i in perguntas:
    for chave , valor in i.items():
        if chave == 'Pergunta':
            print(chave ,':', valor)
        elif chave == 'Opções':
            qtd_quest=  len(valor) - 1
            for i in valor:
                caractere = chr(count)
                print(f"{caractere})" , i)
                count += 1    
        elif chave== 'Resposta':
            resposta = input("Resposta: ")
            if resposta == valor :
                print('Você acertou!!!')
                count_acertos+=1
            else:
                print('Resposta errada')    
        count =  97
    
    
print(f'Você acertou {count_acertos} de {qtd_quest} perguntas')    