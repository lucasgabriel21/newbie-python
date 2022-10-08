# Autor: Lucas Gabriel
# Data de Criação: 10/04/2021
# Programa revela a frequência de letras
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

N = int(input()) # quantidade de casos no teste
entradas = 0

while entradas < N:

    texto = input()
    texto = texto.lower()
    ocorrencias = [] # lista que ordena o número de ocorrências de cada letra do alfabeto
    entradas = entradas + 1

    for letra in alfabeto:
        ocorrencias.append(texto.count(letra))

    x = ocorrencias[:] # cópia da lista de ocorrencias
    x.sort() # organização em ordem crescente de ocorrência

    x1 = [indice for indice,elemento in enumerate(ocorrencias) if elemento ==  x[-1]]
    # x1 é uma lista dos indices (posições) das letras que mais se repetem na lista ocorrencias
    # encontrando a posição das letras que mais se repetem basta acessá-las por alfabeto[posicao]

    saida = []
    for posicao in x1:
        saida.append(alfabeto[posicao])
    print(''.join(saida))