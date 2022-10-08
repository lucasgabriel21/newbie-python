# Autor: Lucas Gabriel
# Data de Criação: 12/05/2021
# Escreva um algoritmo que leia um inteiro N (0 ≤ N ≤ 100),
# correspondente a ordem de uma matriz M de inteiros, e construa a matriz

N = int(input()) #ordem da matriz quadrada
matriz = []

while N != 0:
    for i in range(N):
        linha = []
        for j in range(N):
#diagonal principal
            if i == j:
                linha.append(1)
#abaixo da diagonal principal
            elif i > j:
                linha.append(i-j+1)
#acima da diagonal principal
            elif i < j:
                linha.append(j-i+1)

        matriz.append(linha)

    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == 0:
                print('  {}   '.format(matriz[i][j]), end = '')
            elif j < len(matriz) - 1:
                print('{}   '.format(matriz[i][j]), end = '')
#retira espaços finais
            else:
                print('{}'.format(matriz[i][j]), end='')
        print('')

    matriz = []
    N = int(input())