# Autor: Lucas Gabriel
# Data de Criação: 12/05/2021
# Construção de matriz com elementos de valor 2^(i+j)

N = int(input()) #ordem da matriz quadrada
matriz = []

while N != 0:
    for i in range(N):
        linha = []
        for j in range(N):
            linha.append(2**(i+j))

        matriz.append(linha)

    maior_valor = str(max(max(matriz)))
    T = len(maior_valor)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = str(matriz[i][j])
            while len(matriz[i][j]) < T:
                matriz[i][j] = ' ' + matriz[i][j]

        print(' '.join(matriz[i]))
    print('')
    matriz = []
    N = int(input())