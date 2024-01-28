
caminho_arquivo = 'aula116.txt'
a= 10*'#'
with open(caminho_arquivo,'w+') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write(a)
    arquivo.write('\n')
    arquivo.seek(0, 0)

with open(caminho_arquivo,'r') as arquivo:
   print(arquivo.read())   