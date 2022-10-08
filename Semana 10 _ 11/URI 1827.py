# Autor: Lucas Gabriel
# Data de Criação: 19/05/2021
# Matriz quadrada IV

while True:
    try:
        N = int(input()) #ordem da matriz quadrada (ímpar)
        matriz = []
        inicio_1 = int(N/3)
        final_1 = N - inicio_1

        # preenchimento com 0
        for i in range(N):
            linha = []
            for j in range(N):
                linha.append('0')
            matriz.append(linha)

        #2 na diagonal principal
        for i in range(N):
            for j in range(N):
                if i == j:
                    matriz[i][j] = '2'

        #3 na diagonal secundaria
        for i in range(N):
            for j in range(N):
                if i+j == N-1:
                    matriz[i][j] = '3'

        #preenchimento com 1
        for i in range(inicio_1,final_1):
            for j in range(inicio_1,final_1):
                matriz[i][j] = '1'

        #preenchimento do 4 no meio
        matriz[int(N/2)][int(N/2)] = '4'

        #impressão
        for i in range(len(matriz)):
            print(''.join(matriz[i]))
        print('')

    except EOFError:
        break