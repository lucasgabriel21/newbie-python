# Autor: Lucas Gabriel
# Data de Criação: 07/04/2021
# Programa que leia um vetor N[20]. Troque o primeiro elemento com o último, o segundo elemento com o penúltimo, etc

N = []

while len(N) <= 19:
    N = N + input().split()
N = [int(numero) for numero in N]

for indice in range((len(N))//2):
    ( N[indice] , N[-indice - 1] ) = ( N[-indice -1] , N[indice] )

for i in range(len(N)):
    print('N[{}] = {}'.format(i, N[i]))