# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa que recebe dois parágrafos e os salva em arquivos diferentes

paragrafo1 = input('Digite um parágrafo: ')
paragrafo2 = input('Digite outro parágrafo: ')

arquivo1 = open('arq1.txt','w')
arquivo1.write(paragrafo1)
arquivo1.close()

arquivo2 = open('arq2.txt','w')
arquivo2.write(paragrafo2)
arquivo2.close()

print('Suas informações foram salvas com sucesso!')