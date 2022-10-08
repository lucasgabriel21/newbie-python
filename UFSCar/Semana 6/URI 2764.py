# Autor: Lucas Gabriel
# Data de Criação: 31/03/2021
# Conversão de formatos de data

data = input() # formato DD/MM/AA
print(data[3:5]+'/'+data[:2]+'/'+data[6:]) # formato MM/DD/AA
print(data[6:]+'/'+data[3:5]+'/'+data[:2]) # formato AA/MM/DD
print(data[:2]+'-'+data[3:5]+'-'+data[6:]) # formato DD-MM-AA