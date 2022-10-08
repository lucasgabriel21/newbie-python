# Autor: Lucas Gabriel
# Data de Criação: 07/04/2021
# O programa deve ler 15 valores e colocá-los em 2 vetores conforme estes valores forem pares ou ímpares
# o tamanho de cada um dos dois vetores é de 5 posições. Cada vez que um dos dois vetores encher,
# deve-se imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos

par = []
impar = []
entradas = 0

while entradas < 15:
    valor = int(input())
    entradas = entradas + 1

    if valor % 2 == 0: # para valores pares
        par = par + [valor]
        if len(par) == 5: # quando o vetor enche
            for indice in range(len(par)):
                print('par[{}] = {}'.format(indice, par[indice]))
            par = [] # ele é impresso e recebe novamente a atribuição vazia

    else: # para valores ímpares
        impar = impar + [valor]
        if len(impar) == 5:
            for indice in range(len(impar)):
                print('impar[{}] = {}'.format(indice, impar[indice]))
            impar = []

for indice in range(len(impar)):
    print('impar[{}] = {}'.format(indice, impar[indice]))

for indice in range(len(par)):
    print('par[{}] = {}'.format(indice, par[indice]))