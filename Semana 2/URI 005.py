# Autor: Lucas Gabriel
# Data de Criação: 04/03/2021

idade_em_dias = int(input()) # quantidade de dias vividos
anos = idade_em_dias // 365
meses = (idade_em_dias % 365) // 30
dias = (idade_em_dias % 365) - (meses * 30)
print('''{} ano(s)
{} mes(es)
{} dia(s)'''.format(anos, meses, dias))