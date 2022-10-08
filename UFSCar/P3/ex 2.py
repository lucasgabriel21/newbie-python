# Autor: Lucas Gabriel
# Data de Criação: 25/05/2021
# Análise de arquivos com notas de alunos

arquivo = open('notas.txt','r')
#calculo da média
soma = 0
linhas = 0
for linha in arquivo:
    linha = linha.split()
    nota = float(linha[1])
    soma = soma + nota
    linhas = linhas + 1
media = soma/linhas
print('Média da turma: {:.1f}'.format(media))
arquivo.close()

arquivo = open('notas.txt','r')
saida1 = open('acimaOuIgualMedia.txt','w')
saida2 = open('abaixoMedia.txt','w')
#análise das notas
for linha in arquivo:
    linha = linha.split()
    nota = float(linha[1])
    if nota >= media:
        saida1.writelines(' '.join(linha)+'\n')
    else:
        saida2.writelines(' '.join(linha)+'\n')

arquivo.close()
saida1.close()
saida2.close()