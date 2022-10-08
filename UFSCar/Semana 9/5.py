# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa informa o número de ocorrências de uma palavra no arquivo

nome_arquivo = input('Insira o nome do arquivo: ')
palavra = input('Digite a palavra desejada: ').lower()

arquivo = open(nome_arquivo,'r')
texto = arquivo.read().lower()
# texto e palavras em caixa baixa para evitar diferenciações indesejadas
ocorrencias = texto.count(palavra)
arquivo.close()

print('A palavra aparece {} vez(es).'.format(ocorrencias))