# Autor: Lucas Gabriel
# Data de Criação: 10/03/2021

[A, B, C] = input().split() # Esse comando cria uma lista e atribui os valores às variáveis respectivas
A = float(A) # Converte o valor nomeado da lista de string para int, ou, no caso, float
B = float(B)
C = float(C)
[A, B ,C] = sorted([A, B ,C], reverse=True) # O comando sorted com reverse organiza os valores em ordem decrescente

if A >= B+C:
    print('NAO FORMA TRIANGULO')

elif A**2 == B**2 + C**2:
    print('TRIANGULO RETANGULO')

elif A**2 > B**2 + C**2:
    print('TRIANGULO OBTUSANGULO')

elif A**2 < B**2 + C**2:
    print('TRIANGULO ACUTANGULO')

if A==B==C:
    print('TRIANGULO EQUILATERO')

elif A==B or A==C or B==C:
    print('TRIANGULO ISOSCELES')