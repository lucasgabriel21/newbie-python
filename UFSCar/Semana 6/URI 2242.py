# Autor: Lucas Gabriel
# Data de Criação: 31/03/2021
# Programa classifica risadas inseridas como simetricas como S e assimetricas como N

risada = input()

for letra in risada:
    if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
        risada = risada.replace(letra,'') # as consoantes foram removidas da risada
risada_inversa = risada[::-1]

if risada == risada_inversa:
    print('S')
else:
    print('N')