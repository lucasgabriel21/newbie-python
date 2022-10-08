# Solicite que o usuário informe o valor do seu salário e o tempo de trabalho em anos.
# Calcule o valor do bônus que o usuário deverá receber considerando que:
# Se o tempo de trabalho for maior ou igual a 5 anos, o bônus será de 20% do salário
# Caso contrário, o bônus será de 10% do salário
# Imprima o valor do novo salário.
salario = float(input('Informe o valor de seu salário: '))
tempo_de_trabalho = int(input('Informe a quantidade de anos trabalhados: '))
if tempo_de_trabalho >= 5:
    bonus = salario*0.2
else:
    bonus = salario*0.1
print('O novo salário é de R$ {:.2f}'.format(salario + bonus))