def simetria(a):
    """Analisa se uma matriz a é simétrica"""
    matriz_t = []

    for j in range(len(a)):
        coluna = []
        for i in range(len(a)):
            coluna.append(a[i][j])
        matriz_t.append(coluna)

    if matriz_t == a:
        resultado = 'A matriz é simétrica'
    else:
        resultado = 'A matriz não é simétrica'

    return resultado
