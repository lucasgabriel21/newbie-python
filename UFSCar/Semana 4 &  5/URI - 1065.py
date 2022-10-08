n0 = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

pares = 0

for n in [n0, n1, n2, n3, n4]:
    if n % 2 == 0:
        pares = pares + 1

print('{} valores pares'.format(pares))