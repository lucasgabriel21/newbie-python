# Construa um programa que solicite que o usuário informe os comprimentos de
# 3 segmentos e determine se um triângulo pode ser formado com os 3
# segmentos, ou seja, se cada lado é menor do que a soma dos outros dois.
# Caso forme um triângulo, verifique o tipo formado, sendo:
# ● Equilátero (todos os lados iguais)
# ● Isósceles (dois lados iguais)
# ● Escaleno (todos os lados diferentes)
seg1 = int(input('Informe o comprimento do segmento 1: '))
seg2 = int(input('Informe o comprimento do segmento 2: '))
seg3 = int(input('Informe o comprimento do segmento 3: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:

    if seg1==seg2==seg3:
        print('Formaremos um triângulo equilátero.')

    elif seg1==seg2 or seg1==seg3 or seg2==seg3:
        print('Formaremos um triângulo isósceles.')

    else:
        print('Formaremos um triângulo escaleno.')

else:
    print('Não podemos formar um triângulo com esses valores.')