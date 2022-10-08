def conversao(m): #1
    """converte um valor em m para dm,cm e mm em uma tupla"""
    dm = 10*m
    cm = 100*m
    mm = 1000*m
    return (dm,cm,mm)

def bissexto(ano): #2
    """Determina se o ano é bissexto ou nao"""
    return (ano%4==0 or ano%400==0 and ano%100!=0) #True ou False

def contador_numeral(txt): #3
    """Retorna quantos numeros tem na string"""
    contador = 0
    for elemento in txt:
        if elemento.isdigit():
            contador += 1
    return contador

def contido_em(seq_ref,seq_gene): #4
    """Analisa se a lista menor(seq_gene) está dentro da maior (seq_ref)"""
    seq_ref = seq_ref[:] #cópia, evita alteração da lista original
    ocorrencias = seq_ref.count(seq_gene[0]) #total de ocorrências de seqgene[0] em seqref
    analises = 0 #ocorrências analisadas
    resultado = False

    while analises < ocorrencias:
        inicio = seq_ref.index(seq_gene[0]) #determina posição do inicio da seqgene na seqref
        if seq_ref[inicio:len(seq_gene)+inicio] == seq_gene: #recorte da seqgene para comparar
            resultado = True
        else:
            seq_ref.remove(seq_gene[0]) #remove o elemento analisado
        analises += 1

    if resultado == True:
        resultado = 'A lista menor está contida na lista maior'
    else:
        resultado = 'A lista menor NÃO está contida na lista maior'

    return resultado

def y_asterisco(h): #5
    """Imprime um y de asteriscos com altura h impar"""
    meio = h//2
    linha = 1

    for n in range(0,meio):
        print('{}*{}*'.format(' '*(linha-1),' '*(h-2*linha)))
        linha += 1

    for n in range(meio,h):
        print('{}*'.format(' '*(linha-1)))
        linha -= 1

def simetria(A): #6
    """Analisa se uma matriz A é simétrica"""
    matriz_t = []

    for j in range(len(A)):
        coluna = []
        for i in range(len(A)):
            coluna.append(A[i][j])
        matriz_t.append(coluna)

    if matriz_t == A:
        resultado = 'A matriz é simétrica'
    else:
        resultado = 'A matriz não é simétrica'

    return resultado

def multiplicacao_matriz(a,b): #7
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

def inserir_texto(doc,txt,N): #8
    """Adiciona um texto txt à linha N do documento"""
    try:
        arquivo = open(doc,'r')
        linhas = arquivo.readlines() #armazena as linhas na lista
        arquivo.close()

        linhas.insert(N-1,'{}\n'.format(txt)) #insere o texto na posição desejada
        arquivo = open(doc,'w')
        arquivo.writelines(linhas) #reescreve o documento com a nova linha
        arquivo.close()

    except: #se o arquivo não for encontrado
        print('Arquivo inexistente!')

def main():
    #chamada da função 1
    conversao(5)
    #