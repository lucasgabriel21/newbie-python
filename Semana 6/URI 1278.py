# Autor: Lucas Gabriel
# Data de Criação: 10/04/2021
# Programa que reimprime palavras com suas linhas justificadas à direita e com apenas um espaço entre elas

N = int(input()) # Número de linhas de texto

while N != 0:

    entradas = 0 # linhas de texto inseridas
    casos = [] # lista dos textos inseridos em cada caso
    tamanho_do_texto = [] # lista de tamanhos de textos inseridos

    while entradas < N:
        texto = input().split() # separa o texto inserido em listas, removendo espaços
        casos.append(' '.join(texto)) # o texto é juntado com apenas um espaço e armazenado entre os casos

        tamanho_do_texto.append(len(' '.join(texto)))
        tamanho_do_texto.sort() # organiza os tamanhos de texto em ordem crescente

        entradas = entradas + 1

    for texto in casos:
        print(texto.rjust(tamanho_do_texto[-1])) # justifica à direita de acordo com o maior texto entre os casos

    N = int(input())

    if N != 0:
        print('')