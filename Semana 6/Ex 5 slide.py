# Leia uma palavra e imprima se ela é palíndrome ou não

palavra = input()
palavra = palavra.upper()

if palavra == palavra[::-1]:
    print('{} é uma palavra palíndrome.'.format(palavra.capitalize()))
else:
    print('{} NÃO é uma palavra palíndrome.'.format(palavra.capitalize()))