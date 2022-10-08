valores = 0
positivos = 0
soma = 0

while valores < 6:
    valor = float(input()) # recebe a entrada de 6 valores (0,6)
    valores = valores + 1 # atualiza os valores para falsear condição de while
    if valor > 0:
        positivos = positivos + 1 # atualiza o numero de positivos
        soma = soma + valor # acumula a soma dos valores positivos
    media = soma / positivos # media é a soma dos positivos / o numero deles

print('{} valores positivos'.format(positivos))
print('{:.1f}'.format(media))