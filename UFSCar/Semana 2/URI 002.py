# Autor: Lucas Gabriel
# Data de Criação: 04/03/2021

X = int(input()) # distância total percorrida (em Km)
Y = float(input()) # total de combustível gasto (l)
consumo_medio = X / Y
print('{:.3f} km/l'.format(consumo_medio))