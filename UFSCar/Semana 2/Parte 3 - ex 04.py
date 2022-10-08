# Faça um programa que calcula o preço total de uma compra de supermercado contendo 3 tipos
# de produtos.
print('Calculador de compras')
n_chocolate = int(input('Numero de barras de chocolate compradas: '))
p_chocolate = float(input('Preço de cada barra de chocolate: '))
n_sorvete = int(input('Numero de potes de sorvete comprados: '))
p_sorvete = float(input('Preço de cada pote de sorvete: '))
n_bolacha = int(input('Numero de pacotes de bolacha comprados: '))
p_bolacha = float(input('Preço de cada pacote de bolacha: '))
preço = n_chocolate * p_chocolate + n_sorvete * p_sorvete + n_bolacha * p_bolacha
print('O valor total da compra é de R$ {:.2f}.'.format(preço))
