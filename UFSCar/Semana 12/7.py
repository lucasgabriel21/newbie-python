def multiplicacao_matriz(a,b):
    """Multiplicação da matriz a pela b"""
    produto = []
    for i in range(len(a)): #percorre linha de a
        linha = []
        for j in range(len(b[0])): #percorre colunas de b
            soma = 0
            for k in range(len(b)): #percorre os elementos para multiplicação
                soma += a[i][k]*b[k][j] #soma elementos para criar a linha
            linha.append(soma)
        produto.append(linha)
    return produto
