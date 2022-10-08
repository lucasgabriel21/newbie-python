# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa para salvar os dados do exercício 8

arquivo = open('tabela.txt','w')
numero_entradas = int(input('Insira quantas entradas terá a tabela: '))
linhas = 0

while linhas < numero_entradas:
    if linhas == (numero_entradas - 1):
        arquivo.write('{}'.format(input('Insira nome, idade, peso e altura separados por espaço: ')))
    else:
        arquivo.write('{}\n'.format(input('Insira nome, idade, peso e altura separados por espaço: ')))
    linhas = linhas + 1

arquivo.close()
print('Suas informações foram salvas com sucesso!')