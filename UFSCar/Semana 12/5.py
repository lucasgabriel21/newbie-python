def y_asterisco(h):
    """Imprime um y de asteriscos com altura h impar"""
    meio = h//2
    linha = 1

    for n in range(0,meio):
        print('{}*{}*'.format(' '*(linha-1),' '*(h-2*linha)))
        linha += 1

    for n in range(meio,h):
        print('{}*'.format(' '*(linha-1)))
        linha -= 1
