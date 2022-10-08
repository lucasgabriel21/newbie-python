# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Cálculo do IMC

tabela = open('tabela.txt','r')

for linha in tabela:
    info = linha.split()
    nome = info[0]
    peso = float(info[2])
    altura = float(info[-1])
    IMC = peso/(altura**2)
    print('O IMC de {} é {:.1f}'.format(nome,IMC))

tabela.close()