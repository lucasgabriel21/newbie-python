# Autor: Lucas Gabriel
# Data de Criação: 31/03/2021
# Programa que limita o número de caracteres no texto

texto = input()

if len(texto) <= 140: # O texto deve ter até 140 caracteres
    print('TWEET')

else:
    print('MUTE')