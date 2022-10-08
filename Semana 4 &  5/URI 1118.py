X = 1

while X == 1:

    A1 = float(input())

    while A1 > 10 or A1 < 0:
        print('nota invalida')
        A1 = float(input())

    A2 = float(input())

    while A2 > 10 or A2 < 0:
        print('nota invalida')
        A2 = float(input())

    media = (A1 + A2) / 2
    print('media = {:.2f}'.format(media))

    print('novo calculo (1-sim 2-nao)')
    X = int(input())

    while X < 1 or X > 2:
        print('novo calculo (1-sim 2-nao)')
        X = int(input())