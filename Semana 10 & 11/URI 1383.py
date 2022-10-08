# Autor: Lucas Gabriel
# Data de Criação: 21/05/2021
# Programa para validação de sudoku


n = int(input()) #numero de matrizes a serem analisadas
m = 1 #numero da instancia
numeral = ['1','2','3','4','5','6','7','8','9']

while m <= n:
    matriz = []
    ordem = 9

    #formacao da tabela do sudoku
    for i in range(ordem):
        matriz.append(input().split())

    #analise das linhas
    resultado = True
    for numero in numeral:
        for linha in matriz:
            if numero not in linha:
                resultado = False

    #se a analise da linha nao encontrar falhas
    if resultado == True:
        matriz_t = [] #matriz transposta
        #formacao da transposta
        for j in range(ordem):
            coluna = []
            for i in range(ordem):
                coluna.append(matriz[i][j])
            matriz_t.append(coluna)

        #analise das colunas atraves da transposta
        for numero in numeral:
            for coluna in matriz_t:
                if numero not in coluna:
                    resultado = False

        #se a analise das colunas nao encontrar falhas
        if resultado == True:
            #criação da lista das 9 submatrizes 3x3
            submatrizes = []
            n_submatrizes = 0

            linha_1 = 0 #linha inicial
            coluna_1 = 0 #coluna inicial
            linha_fim = 3 #linha final
            coluna_fim = 3 #coluna final
            while n_submatrizes < 9:
                submatriz = []
                #algoritmo de formacao de submatriz
                for i in range(linha_1,linha_fim):
                    for j in range(coluna_1,coluna_fim):
                        submatriz.extend(matriz[i][j])

                coluna_1 = coluna_1 + 3
                coluna_fim = coluna_fim + 3
                n_submatrizes = n_submatrizes + 1
                submatrizes.append(submatriz)

                if n_submatrizes == 3 or n_submatrizes == 6:
                    linha_1 = linha_1 + 3
                    coluna_1 = 0
                    linha_fim = linha_fim + 3
                    coluna_fim = 3

            #analise dos elementos das submatrizes
            for numero in numeral:
                for submatriz in submatrizes:
                    if numero not in submatriz:
                        resultado = False

            if resultado == True:
                print('Instancia {}'.format(m))
                print('SIM')
                print('')

    if resultado == False:
        print('Instancia {}'.format(m))
        print('NAO')
        print('')

    m = m + 1