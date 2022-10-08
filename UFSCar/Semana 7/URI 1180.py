# Autor: Lucas Gabriel
# Data de Criação: 07/04/2021
# Apresentar o menor valor de um elemento do vetor X de tamanho N e a sua posição

N = int(input()) # tamanho do vetor
X = input().split() # vetor que será preenchido com N elementos
X = [int(numero) for numero in X]

min = X[:] # clone da lista X
min.sort() # ordena do menor para o maior inteiro da lista identica a X

print('Menor valor: {}'.format(min[0])) # menor valor da lista
print('Posicao: {}'.format(X.index(min[0]))) # posição em X