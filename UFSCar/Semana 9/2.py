# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa que exibe o número de linhas de um arquivo

arquivo = open('layla.txt','r')
lista = arquivo.readlines()
# Cada linha se torna um elemento da lista
print('O arquivo tem {} linhas.'.format(len(lista)))
arquivo.close()