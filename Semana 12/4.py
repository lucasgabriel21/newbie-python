def contido_em(seq_ref,seq_gene):
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
