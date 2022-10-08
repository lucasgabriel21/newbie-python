# Representada por conjunto de elementos constantes separados por vírgula
# Utilizam ( ) ao invés de [ ] para a representação do conjunto EX: A = (1,2,3)
# Os elementos da tupla também podem ser acessados por índices
# Tuplas são IMUTÁVEIS

# As operações serão idênticas às das listas, com exceção daquelas que alteram o elemento: append, del e extend

# Permutação de valores entre variáveis, ex:
a,b = b,a # troca os valores entre a e b

# Criação de tuplas a partir de listas, ex:
L=[1,2,3]
T = tuple(L)
print(T) # imprime a tupla (1,2,3)

# Tuplas aceitam dados heterogêneos e listas dentro de tuplas ainda podem ser modificadas