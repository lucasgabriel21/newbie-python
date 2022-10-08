# Autor: Lucas Gabriel
# Data de Criação: 07/04/2021
# É lido um valor X que fica na primeira posição de um vetor N[100]. Em cada posição subsequente de N (1 até 99)
# coloca-se a metade do valor armazenado na posição anterior

X = float(input())
N = [X]
indice = 0

while len(N) < 100:
    N.append(N[indice]/2)
    indice = indice + 1

for i in range(len(N)):
    print('N[{}] = {:.4f}'.format(i, N[i]))