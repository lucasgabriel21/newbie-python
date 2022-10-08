# Autor: Lucas Gabriel
# Data de Criação: 04/03/2021

N = int(input()) # tempo de duração em segundos de um determinado evento
horas = N // 3600 # divisão inteira de segundos em horas
minutos = (N % 3600) // 60 # o resto dos segundos da hora divididos em minutos
segundos = (N % 3600) - (minutos * 60) # o resto dos segundos da hora menos o que já está em minutos
print('{}:{}:{}'.format(horas,minutos,segundos))