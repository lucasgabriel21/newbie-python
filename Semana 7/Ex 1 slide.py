# Leia duas listas de 10 números inteiros cada. Em seguida, gere e imprima uma
# terceira lista que contém, para os índices pares, elementos da primeira lista e,
# para os índices ímpares, elementos da segunda lista

n = 0
m = 0
A = []
B = []
Res = ['','','','','','','','','','']

while n < 10:
    A.append(int(input('Insira um valor para a lista 1: ')))
    n = n + 1

while m < 10:
    B.append((int(input('Insira um valor para a lista 2: '))))
    m = m + 1

for i in range(len(Res)):

    if i % 2 == 0:
        Res[i] = A[i]

    else:
        Res[i] = B[i]

print('A = {}'.format(A))
print('B = {}'.format(B))
print('Res = {}'.format(Res))