# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Leitura das informações

tabela = open('tabela.txt','r')

for linha in tabela:
    info = linha.split()
    nome = info[0]
    idade = info[1]
    peso = info[2]
    altura = info[-1]
    print('Nome: {}\nIdade: {}\nPeso: {} kg\nAltura: {} m\n'.format(nome,idade,peso,altura))

tabela.close()