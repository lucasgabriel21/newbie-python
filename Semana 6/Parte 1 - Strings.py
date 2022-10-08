# Dado composto por conjunto de caracteres

# Indexação
palavra = abracadabra
palavra[1] # retorna 'b'

# Fatiamento
palavra[4:7] # retorna 'cad'

# Operador in
'braca' in palavra # retorna True

# Operadores de comparação
'abra' < 'cadabra' # comparação alfabética, True
'abra' < 'CADABRA' # False, maiúsculas vêm primeiro

# Operadores + e *
'abra'+'cadabra' # 'abracadabra'
'-'*10 # '----------' 10 traços

# Função len
len(palavra) # tamanho da palavra é 11 letras