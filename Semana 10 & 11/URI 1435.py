# Autor: Lucas Gabriel
# Data de Criação: 19/05/2021
# Matriz quadrada 1

N = int(input()) #ordem da matriz quadrada

while N!=0:
    matriz = []
    valor = 1 #valor do exterior (bordas)

    if N%2==0:
        maior_valor = N/2
    else:
        maior_valor = (N+1)/2

    for i in range(N):
        linha = []
        for j in range(N):
            linha.append('')
        #preenchimento dos espaços na matriz
        matriz.append(linha)

    linha_inicial = 0 #linha superior
    linha_final = N-1 #linha inferior
    coluna_inicial = 0 #coluna mais à esquerda
    coluna_final = N-1 #coluna mais à direita

    while valor <= maior_valor:

        x = coluna_inicial
    #escrevendo os valores na primeira e última linhas
    #percorrendo horizontalmente (por colunas)
        while x <= coluna_final:
            matriz[linha_inicial][x] = valor
            matriz[linha_final][x] = valor
            x = x + 1

        x = linha_inicial
    #escrevendo os valores na primeira e última colunas
    #percorrendo verticalmente (por linhas)
        while x <= linha_final:
            matriz[x][coluna_inicial] = valor
            matriz[x][coluna_final] = valor
            x = x + 1

        valor = valor + 1
    #redução de ordem da matriz
        linha_inicial = linha_inicial + 1
        linha_final = linha_final - 1
        coluna_inicial = coluna_inicial + 1
        coluna_final = coluna_final - 1

    for i in range(N):
        linha = ''
        for j in range(N):
            linha = linha + '{:4d}'.format(matriz[i][j])
        print(linha[1:])
    print('')

    N = int(input()) #ordem da matriz quadrada