def inserir_texto(doc,txt,N):
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
