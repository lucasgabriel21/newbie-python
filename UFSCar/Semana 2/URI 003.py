# Autor: Lucas Gabriel
# Data de Criação: 04/03/2021

autonomia = 12 # km/l
tempo = int(input()) # tempo gasto na viagem (em horas)
vm = int(input()) # velocidade média durante a mesma (em km/h)
distancia = vm * tempo # resultado em km
litros_necessarios = distancia / autonomia # [km]/[km/l]=l
print('{:.3f}'.format(litros_necessarios))