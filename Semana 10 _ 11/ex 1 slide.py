# Criar um programa para ler uma matriz através da entrada do teclado e depois imprime.
# Primeiro a entrada deve ser o número de linhas (L) e colunas (C). Depois cada entrada é um elemento da lista.

entrada = input('Insira o número de linhas e colunas, respectivamente, '
                    'separados por espaço: ').split()
L = int(entrada[0])
C = int(entrada[1])
matriz = []

for linhas in range(L):
    linha = input().split()

    for j in range(len(linha)):
        if j >= C:
            linha.remove(linha[j])

    matriz.append(linha)

for linha in matriz:
    print('{}'.format(' '.join(linha)))