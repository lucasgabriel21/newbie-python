# Autor: Lucas Gabriel
# Data de Criação: 10/03/2021

[N1, N2, N3, N4] = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

MEDIA = (N1*2 + N2*3 + N3*4 + N4*1)/10
print('Media: {:.1f}'.format(MEDIA))

if MEDIA>=7.0:
    print('Aluno aprovado.')

if MEDIA<5.0:
    print('Aluno reprovado.')

if MEDIA >= 5.0 and MEDIA <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: {:.1f}'.format(nota_exame))
    MEDIA = (MEDIA + nota_exame)/2
    if MEDIA>=5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(MEDIA))