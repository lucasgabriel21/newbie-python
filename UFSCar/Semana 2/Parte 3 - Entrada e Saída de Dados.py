# Entrada de dados
# função input(), recebe o argumento inserido pelo usuário sempre como string
# exemplo 1
entrada = input('Insira o argumento para ser usado no programa')
nome = input("Informe o seu nome: ")
# *quando for utilizar números sempre se lembrar de converter a str em int ou float
# através de comandos como int(input()) ou float(input())
# exemplo 2
a = input("Primeiro número inteiro: ") # mostra o texto para o usuário responder
b = input("Segundo número inteiro: ") # novamente, o usuário responde
c = a + b # concatenação das strings a e b
a = int(a) # conversão para inteiro
b = int(b) # conversão para inteiro
c = a + b # soma dos inteiros a e b

# Saída de dados
# função print(), apresenta na tela os dados computados para o usuário
# exemplo 1
nome=input("Informe o seu nome: ") #entrada
print("Saída de dados") # saida
print(nome) # saida
print("Nome:",nome) # saida

# operador de composição (%), há um marcador para cada classe:
# %s (string) | %d (int) | %f (float)
# atua como marcador de posição para posterior substituição
# exemplo 2
idade = 19
nome = "João"
saldo = 200.5
print("%s tem %d anos" % (nome,idade))
print("%s tem R$ %.2f no bolso" % (nome,saldo))

# Método format (substitui o %)
# marcação de posição utilizando {}
# exemplo 3
idade =19
nome = "João"
saldo = 5.444444
print("{} tem {} anos".format(nome,idade))
print("{} tem R$ {:.2f} no bolso".format(nome,saldo))