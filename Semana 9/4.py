# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa lê dois arquivos e escreve o conteúdo em um terceiro

arquivo_1 = open('layla.txt','r')
texto_1 = arquivo_1.read()
arquivo_1.close()

arquivo_2 = open('layla_2.txt','r')
texto_2 = arquivo_2.read()
arquivo_2.close()

lista = [texto_1,'\n',texto_2]

arquivo_3 = open('layla_final.txt','w')
arquivo_3.writelines(lista)
arquivo_3.close()

print('Suas informações foram salvas com sucesso!')