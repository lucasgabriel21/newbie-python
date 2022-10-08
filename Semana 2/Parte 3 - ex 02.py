# Escreva um programa que peça que o usuário informe a quantidade de
# dias, horas, minutos e segundos. Calcule e imprima o total em segundos.
d = int(input('Insira o número de dias: '))
h = int(input('Insira o número de horas: '))
m = int(input('Insira o número de minutos: '))
s = int(input('Insira o número de segundos: '))
d  = d*86400
h = h*60**2
m = m*60
s = s*1
total = d + h + m + s
print('O total foi de {} segundos.'.format(total))
