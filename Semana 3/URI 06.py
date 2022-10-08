# Autor: Lucas Gabriel
# Data de Criação: 10/03/2021

salario = float(input())

if 0 <= salario <= 400:
    reajuste = 0.15*salario

if 400 < salario <= 800:
    reajuste = 0.12*salario

if 800 < salario <= 1200:
    reajuste = 0.1*salario

if 1200 < salario <= 2000:
    reajuste = 0.07*salario

if salario > 2000:
    reajuste = 0.04*salario

print('Novo salario: {:.2f}'.format(salario + reajuste))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {:.0f} %'.format((reajuste/salario)*100))