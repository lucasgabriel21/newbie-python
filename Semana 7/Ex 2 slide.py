# Escreva um programa que leia a idade e o gênero ("M" para masculino e "F"
# para feminino) de um grupo de 100 pessoas. Calcule e imprima:
# ○ o total de mulheres
# ○ o total de homens
# ○ média das idades das pessoas do grupo
# ○ média das idades dos homens
# ○ o total de homens com idade maior do que a média das idades dos homens do grupo

pessoas = 0
meta = 100
soma_idades = 0
idades = []
generos = []

while pessoas < meta:
    idades.append(int(input('Digite a idade: ')))
    generos.append(input('Gênero M ou F? '))
    pessoas = pessoas + 1

total_mulheres = generos.count('F')
total_homens = generos.count('M')

for numero in idades:
    soma_idades = soma_idades + numero

media_idades = soma_idades / pessoas
soma_idades = 0

idades_homens = [idade_M for indice,idade_M in enumerate(idades) if generos[indice] == 'M']

for numero in idades_homens:
    soma_idades = soma_idades + numero

media_idades_homens = soma_idades / total_homens
acima_da_media = [idade for idade in idades_homens if idade > media_idades_homens]

print('O total de mulheres é {}'.format(total_mulheres))
print('O total de homens é {}'.format(total_homens))
print('Média das idades das pessoas: {:.1f}'.format(media_idades))
print(('Média de idade masculina: {:.1f}'.format(media_idades_homens)))
print('Homens com idade acima da média: {}'.format(len(acima_da_media)))