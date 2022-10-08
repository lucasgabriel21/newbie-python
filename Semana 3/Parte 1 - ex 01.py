# Leia as notas de duas provas de um aluno e calcule a média. O valor máximo de cada prova é 10.0.
# Considerando a média de aprovação 6.0, imprima uma mensagem informando a média do aluno e se ele foi aprovado ou não
p1 = float(input('Nota da primeira prova: '))
p2 = float(input('Nota da segunda prova: '))
media = (p1+p2)/2
print('A sua média foi {:.1f}'.format(media))
if media >= 6:
    print('Você foi aprovado!')
else:
    print('Você não foi aprovado.')