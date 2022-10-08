# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa que lê o conteúdo de um arquivo

arquivo = open('layla.txt','r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()