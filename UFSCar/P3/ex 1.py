# Autor: Lucas Gabriel
# Data de Criação: 25/05/2021
# Análise de matriz quadrada

n = int(input()) #ordem da matriz quadrada
m = 1 #numero da instancia

while n != 0:
    matriz = []
    for i in range(n):
        matriz.append(input().split())

    #elemento de menor valor
    matriz_copia = [linha[:] for linha in matriz]
    menores_valores = []
    for linha in matriz_copia:
        linha.sort()
        menor_valor_linha = linha[0]
        menores_valores.extend(menor_valor_linha)
    menores_valores.sort()
    menor_valor = menores_valores[0]

    #posição do elemento e média da diagonal principal
    soma = 0
    pos_coluna = -1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if pos_coluna == -1:
                if matriz[i][j] == menor_valor:
                    pos_linha = i
                    pos_coluna = j
            if i == j:
                soma = soma + int(matriz[i][j])
    print('Instância {}'.format(m))
    print('Menor:{} (linha:{}, coluna:{})'.format(menor_valor,pos_linha,pos_coluna))
    print('Média da diagonal principal: {:.2f}'.format(soma/n))

    m = m + 1
    n = int(input())