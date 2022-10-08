# Autor: Lucas Gabriel
# Data de Criação: 10/03/2021

horarios = input().split()
[Hi, Hf] = horarios
Hi = int(Hi)
Hf = int(Hf)

if Hf > Hi:
    duracao = Hf - Hi
elif Hf == Hi:
    duracao = 24
else:
    duracao = (24 + Hf) - Hi
print('O JOGO DUROU {} HORA(S)'.format(duracao))