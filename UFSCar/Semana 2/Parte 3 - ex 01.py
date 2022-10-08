# Escreva um programa que peça que o usuário informe  um número de
# dias. Calcule e imprima o número de anos, meses e dias correspondente
# ao número de dias informado. Considere todos os anos com 365 dias e
# todos meses com 30 dias.
n = int(input('Insira um número de dias: '))
anos = (n // 365)
meses = (n % 365) // 30
dias = n % 365 - 30*meses
print('O valor informado corresponde a {} ano(s), {} mes(es) e {} dia(s).'.format(anos, meses, dias))