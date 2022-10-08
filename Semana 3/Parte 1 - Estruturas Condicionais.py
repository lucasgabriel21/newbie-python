# Usadas para executar passos que dependem de verificação de condições
# Condição é dada como expressão booleana (True ou False)
# São formados blocos de comando sob 'if' e (opcionalmente) 'else', marcados pelo recuo do texto para a direita
# Exemplo 1: Solicite a entrada de dois números inteiros a e b. Imprima o maior:
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
if a>b:
    print(a)
else:
    if b>a:
        print(b)
    else:
        print('Os números são iguais')
print()

# Comandos if aninhados:
# Modo 1:
if (x < y):
    statements_a
else:
    if(x>y):
        statements_b
    else:
        statements_c
print()
# Modo 2:
if (x < y):
    statements_a
elif (x>y): # Pode haver vários comandos elif, mas apenas um comando else. A primeira condição verdadeira é executada
    statements_b
else:
    statements_c
