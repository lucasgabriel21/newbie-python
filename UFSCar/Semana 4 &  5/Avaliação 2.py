# Autor: Lucas Gabriel
# Data de Criação: 30/03/2021
# Programa de classificação etária

idade = 1
pessoas = 0
faixa1 = 0 # 0 a 15 anos
faixa2 = 0 # 16 a 30 anos
faixa3 = 0 # 31 a 45 anos
faixa4 = 0 # 46 a 60 anos
faixa5 = 0 # > 60 anos

while idade != 0:
    idade = int(input())

    if 0 < idade <= 15:
        faixa1 = faixa1 + 1
        pessoas = pessoas + 1
    elif 15 < idade <= 30:
        faixa2 = faixa2 + 1
        pessoas = pessoas + 1
    elif 30 < idade <= 45:
        faixa3 = faixa3 + 1
        pessoas = pessoas + 1
    elif 45 < idade <= 60:
        faixa4 = faixa4 + 1
        pessoas = pessoas + 1
    elif idade > 60:
        faixa5 = faixa5 + 1
        pessoas = pessoas + 1

print(faixa1)
print(faixa2)
print(faixa3)
print(faixa4)
print(faixa5)
print('{:.1f}'.format(100*(faixa1 + faixa2)/pessoas))