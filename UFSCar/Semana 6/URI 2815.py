# Autor: Lucas Gabriel
# Data de Criação: 02/04/2021
# Programa elimina redundâncias de palavras com primeira sílaba repetida

texto = input().split() # Separando as palavras do texto em uma lista

for indice in range(len(texto)): # Cada elemento da lista é percorrido por seu índice
    palavra = texto[indice] # Cada palavra está ligada a um índice da lista 'texto'

    if palavra[0:2] == palavra[2:4]: # Se as duas primeiras sílabas de uma palavra forem iguais...
        palavra = palavra.capitalize() # Diferencia as duas primeiras sílabas para substituir apenas uma ocorrência
        texto[indice] = palavra.replace(palavra[0:2], '') # Aquela palavra é atualizada, removendo a primeira sílaba

print(' '.join(texto)) # É o inverso da função split e converte novamente a lista em texto