n = int(input())
inst = 1

while n != 0:
    matriz_A = []
    for i in range(n):
        matriz_A.append(input().split())
    matriz_T = []
    for j in range(n):
        coluna = []
        for k in range(n):
            coluna.append(matriz_A[k][j])
        matriz_T.append(coluna)

    c = []
    for l in matriz_T:
        l.sort()
        menor = l[0]
        c.extend(menor)

    c = [int(valor) for valor in c]
    soma = 0
    for v in c:
        soma = soma + v

    media = soma / n
    print('Instância {}'.format(inst))

    inst = inst + 1