# Operadores são utilizados para cálculos, comparações e expressões lógicas
# Tipos: Aritméticos, Relacionais e Lógicos

# Operadores aritméticos
# + (adição) | - (subtração) | * (multiplicação) | / (divisão fracionária)
# // (divisão inteira) | % (resto) | ** (potenciação)
#exemplo
a = 2 + 3 # a recebe o resultado da adição -> a = 5
A = 6-2 # A recebe o resultado da subtração -> A = 4
a = 2 * 5 # a recebe o resultado da multiplicação -> a = 10
b = 11/5 # b recebe o resultado da divisão -> b = 2.2
c = 11//5 # c recebe o resultado da divisão inteira -> c = 2
d = 11%5 # d recebe o resto da divisão -> d = 1
e = 2**3 # e recebe o resultado da potenciação -> e = 8
a = a + 1 # a tem seu valor anterior atualizado por uma soma -> a = 11
# As regras de operação são as mesmas da matemática
# Exercício 1. Escreva um programa para o problema: Considerando que João tem um
# salário de R$1500,50 , atualize o valor do salário de João considerando
# uma taxa de aumento de 5%.
salario = 1500.50
aumento = 5/100
salario = salario + (salario * aumento)
print(salario)

# Operadores relacionais
# == (igualdade) | != (diferente) | > (maior)
# < (menor) | >= (maior ou igual) | <= (menor ou igual)
#exemplo
a = 3 > 2 # a recebe o resultado da comparação: True
b = 3 == 2 # b também recebe o resultado de uma comparação: False

# Operadores lógicos
# not (negação) | and (conjunção) | or (disjunção)
# A tabela verdade reúne todas as possibilidades de valores envolvidos numa expressão
# Ordem de precedência 1st NOT | 2nd AND | 3rd OR

# Ordem de precedência entre os três operadores:
# 1st Aritméticos | 2nd Relacionais | 3rd Lógicos