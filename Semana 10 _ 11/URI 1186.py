# Autor: Lucas Gabriel
# Data de Criação: 12/05/2021
# Leitura de matriz e cálculo de soma ou média dos valores abaixo
# da diagonal secundária

O = input() #'S' para soma ou 'M' para média
matriz = []
ordem = 12

#entrada dos dados da matriz
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(float(input()))
    matriz.append(linha)

#região abaixo da diagonal secundária
soma = 0
elementos = 0
for i in range(ordem):
    for j in range(ordem):
#elementos na diag secundária possuem
# i+j=ordem da matriz quadrada-1 (contando do 0)
        if i + j > ordem - 1:
            soma = soma + matriz[i][j]
            elementos = elementos + 1

if O == 'S':
    print('{:.1f}'.format(soma))

elif O == 'M':
    print('{:.1f}'.format(soma / elementos))