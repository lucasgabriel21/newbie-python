# Autor: Lucas Gabriel
# Data de Criação: 12/05/2021
# Leitura de matriz e cálculo de soma ou média dos valores da linha

L = int(input()) #linha escolhida
T = input() #'S' para soma ou 'M' para média
matriz = []

ordem = 3 #ordem da matriz quadrada

#entrada dos dados da matriz
for i in range(ordem): #percorre linhas
    linha = []
    for j in range(ordem): #percorre colunas
        linha.append(float(input()))
    matriz.append(linha)

#soma dos valores de uma linha
soma = 0
for elemento in matriz[L]:
    soma = soma + elemento

#apresenta a soma
if T == 'S':
    print('{:.1f}'.format(soma))

#apresenta a média
elif T == 'M':
    print('{:.1f}'.format(soma/ordem))