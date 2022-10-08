# Deseja-se publicar o número de acertos de cada aluno em uma prova em
# forma de testes. A prova consta de 10 questões, cada uma com cinco
# alternativas identificadas por A, B, C, D e E. Para isso devem ser lidos:
# ● cartão gabarito
# ● número de alunos da turma
# ● cartão de respostas de cada aluno
# Escreva um programa que mostre as notas de cada aluno, considerando que cada questão vale 1 ponto.
# Imprima também a média da turma, com precisão de duas casas decimais.

gabarito = ['','','','','','','','','','']
alunos = int(input('Número de alunos na turma: '))
notas = []
soma_notas = 0

for i in range(len(gabarito)):
    gabarito[i] = input('Resposta da questão {}: '.format(i + 1))

for aluno in range(alunos):
    cartao_resposta = input('Insira as respostas de cada questão separadas por espaço: ').split()
    corretas = [resposta for i,resposta in enumerate(cartao_resposta) if cartao_resposta[i] == gabarito[i]]
    print('Nota do {}º aluno: {}'.format((aluno + 1), len(corretas)))
    notas.append(len(corretas))

for nota in notas:
    soma_notas = soma_notas + nota

print('A média da turma foi de {:.2f} pontos'.format(soma_notas / alunos))