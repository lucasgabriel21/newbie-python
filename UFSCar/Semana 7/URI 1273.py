# Autor: Lucas Gabriel
# Data de Criação: 10/04/2021
# Programa que reimprima palavras com suas linhas justificadas à direita

N = int(input())

while N != 0:

    entradas = 0  # quantidade de entradas de texto
    casos = []  # lista dos inputs de cada caso de teste
    tamaho_das_palavras = []  # lista o tamanho de cada palavra do caso de teste em avaliação

    while entradas < N: # recebe inputs até igualar N entradas
        texto = input()
        casos.append(texto)

        tamaho_das_palavras.append(len(texto))
        tamaho_das_palavras.sort() # organiza os tamanho de palavras em ordem crescente

        entradas = entradas + 1

    for palavra in casos:
        print(palavra.rjust(tamaho_das_palavras[-1])) # justifica a palavra à direita com o maior tamanho de palavra no caso

    N = int(input())

    if N != 0:
        print('')