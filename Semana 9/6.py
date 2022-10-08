# Autor: Lucas Gabriel
# Data de Criação: 05/05/2021
# Programa imprime os nomes de alunos com mais de 6 notas
# calcula a nota mínima, a máxima e a média das notas de cada estudante
# imprime o nome, as notas mínima e máxima e a média de cada estudante

arquivo = open('notas_estudantes.dat','r')
linhas = 0
nomes = [] # Nomes dos alunos com mais notas

while linhas < 5:
    dados = arquivo.readline().split() # Dados de uma linha listados
    linhas = linhas + 1

    if len(dados) > 6: # Quantidade de notas
        nomes.append(dados[0]) # Nomes armazenados na lista

# Criação da lista de notas apenas com os inteiros contidos em dados
    notas = [int(dados[i]) for i in range(len(dados)) if dados[i].isdigit()]
    notas.sort() # ordem crescente
    nota_min = notas[0]
    nota_max = notas[-1]
    soma = 0

    for numero in notas:
        soma = soma + numero
    media = soma / len(notas)

    print('Nome: {}\nNota mínima: {}\nNota máxima: {}\nMédia: {:.1f}\n'.format(dados[0],nota_min,nota_max,media))

print('Alunos com 6 notas ou mais: {}.'.format(', '.join(nomes)))