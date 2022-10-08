# Autor: Lucas Gabriel
# Data de Criação: 30/03/2021

[pais, vinho, valor_compra] = input().split()
valor_compra = float(valor_compra)

if pais == 'IT':
    preço_venda = valor_compra * 1.9

elif pais == 'FR':
    if vinho == 'B':
        preço_venda = valor_compra * 1.8
    else:
        preço_venda = valor_compra * 1.75

elif pais == 'ES':
    preço_venda = valor_compra * 1.4

elif pais == 'PT':
    if vinho == 'T':
        preço_venda = valor_compra * 1.75
    elif vinho == 'R':
        preço_venda = valor_compra * 1.80
    else:
        preço_venda = valor_compra * 1.70

print('{:.2f}'.format(preço_venda))

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