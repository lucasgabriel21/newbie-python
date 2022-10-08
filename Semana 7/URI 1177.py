# Autor: Lucas Gabriel
# Data de Criação: 07/04/2021
# Programa que lê um valor T e preenche um vetor N[1000] com a sequência de valores de 0 até T-1

T = int(input())
N = []

while len(N) < 1000:

    for numero in range(T): # Enquanto a lista não atingir 1000 elementos segue-se adicionando numeros de 0 a T-1
        if len(N) < 1000:
            N = N + [numero]

N = [int(numero) for numero in N]

for indice in range(len(N)):
    print('N[{}] = {}'.format(indice, N[indice]))