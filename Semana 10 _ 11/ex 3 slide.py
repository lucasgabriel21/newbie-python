# Criar um programa para fazer multiplicação de matriz

a = [[1,2,3],
     [3,4,5],
     [5,6,7]]

b = [[1,1,2],
     [2,2,4],
     [3,3,6]]

produto = []

num_linhas = len(a)
num_colunas = len(a[0])

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        soma = 0
        for k in range(num_colunas):
            soma = soma + a[i][k] * b[k][j]
        linha.append(soma)
    produto.append(linha)

for i in range(num_linhas):
    for j in range(num_colunas):
        print('{} '.format(produto[i][j]), end = '')
    print('')