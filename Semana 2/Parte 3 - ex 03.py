# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte o nome, a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada
# cigarro, calcule quantos dias de vida o fumante perdeu.
# Exiba uma mensagem direcionada ao usuário, informando o total em dias.
nome = input('Insira o seu nome: ')
qtd = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Ha quantos anos e fumante? '))
dias_perdidos = ((10 * qtd) * 365 * anos) // 1440
print('Boa noite {}, devido ao tabagismo voce perdeu {} dias de vida.'.format(nome, dias_perdidos))