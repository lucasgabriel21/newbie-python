# Autor: Lucas Gabriel
# Data de Criação: 18/05/2021
# Impressora de matrizes

while 0==0:
    try:
        N = int(input()) #ordem da matriz quadrada
        matriz = []

        for i in range(N):
            linha = []
            for j in range(N):
            #diagonal secundária
                if i+j==N-1:
                    linha.append('2')
            #diagonal principal
                elif i==j:
                    linha.append('1')
            #no resto fica 3
                else:
                    linha.append('3')

            matriz.append(linha)

        for i in range(len(matriz)):
            print('{}'.format(''.join(matriz[i])))

    except EOFError:
        break