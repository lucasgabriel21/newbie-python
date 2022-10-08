N1 = float(input())

while N1 < 0 or N1 > 10 : # não valida a nota enquanto não estiver em [0, 10]
    print('nota invalida')
    N1 = float(input())

N2 = float(input())

while N2 < 0 or N2 > 10 :
    print('nota invalida')
    N2 = float(input())

print('media = {:.2f}'.format(( N1 + N2 ) / 2))