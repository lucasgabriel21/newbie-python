# Criar um programa que verifica se uma matriz tem ao menos duas linhas idênticas.
# Caso encontre duas linhas idênticas deve imprimir na tela a mensagem “contém duas
# linhas idênticas” e se não contém imprimir “não contém duas linhas idênticas”.

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

analise_linha = []
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j != i:
            if matriz[i] == matriz[j]:
                analise_linha.append('S')

if analise_linha != []:
    print('Contém ao menos duas linhas idênticas.')
else:
    print('Não contém linhas idênticas.')