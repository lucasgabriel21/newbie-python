alcool = 0
gasolina = 0
diesel = 0
codigo = 0

while codigo != 4:
    codigo = int(input())

    while codigo < 1 or codigo > 4:
        codigo = int(input())

    if codigo == 1:
        alcool = alcool + 1

    elif codigo == 2:
        gasolina = gasolina + 1

    elif codigo == 3:
        diesel = diesel + 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))