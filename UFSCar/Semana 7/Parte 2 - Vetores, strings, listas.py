# Diferenças de vetores com relação a listas: dados homogêneos, tamanho pré-definido, módulo array

# Operadores lógicos:
# in e not in retornam True ou False para a ocorrência de um item na lista

# Apelido de listas: quando dois nomes distintos fazem referência à mesmas lista, modificar um deles alterará o outro

# Para evitar o conflito de apelidos pode-se clonar a lista com o fatiamento [:]

# Comando del remove um elemento da lista acessado pelo índice

# List comprehensions: [<expressão> for <item> in <sequência> if <condição>]
# ex:
L1 = [-1,3,-4,-9,5]
L2= [n*2 for n in L1 if n>0] # cria a lista [6,10]

# .split() separa uma string em lista, .join() junta os elementos da lista em uma frase (str)
# .list() transforma qualquer input em lista, separando elemento por elemento, letra por letra