operaçao = input('Informe uma operação dentre (+, -, * ou /) ou 0 para encerrar: ')

while operaçao != '0':
    if operaçao == '+':
        for numero in range(1, 11):
            print('\nTabuada do {}\n'.format(numero))
            for n in range(1, 11):
                print('{} + {} = {}'.format(numero, n, numero + n))

    elif operaçao == '-':
        for numero in range(1, 11):
            print('\nTabuada do {}\n'.format(numero))
            for n in range(1, 11):
                print('{} - {} = {}'.format(numero, n, numero - n))

    elif operaçao == '*':
        for numero in range(1, 11):
            print('\nTabuada do {}\n'.format(numero))
            for n in range(1, 11):
                print('{} x {} = {}'.format(numero, n, numero * n))

    elif operaçao == '/':
        for numero in range(1, 11):
            print('\nTabuada do {}\n'.format(numero))
            for n in range(1, 11):
                print('{} / {} = {:.2f}'.format(numero, n, numero / n))

    else:
        print('Entrada inválida!')

    operaçao = input('Informe uma operação dentre (+, -, * ou /) ou 0 para encerrar: ')

print('Operações encerradas.')